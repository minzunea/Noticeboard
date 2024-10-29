from django.shortcuts import render, get_object_or_404, redirect
from .models import Create, Comment
from django.core.paginator import Paginator  


def index(request):
    page = request.GET.get('page', '1') # 페이지 구현
    text_list = Create.objects.order_by('-create_date')
    paginator = Paginator(text_list, 5) # 10개 씩
    page_obj = paginator.get_page(page)
    content = {'text_list':page_obj,}
    return render(request, "board/index.html", content)

def detail(request, text_id):
    text_list = get_object_or_404(Create, pk=text_id)
    comment_list = Comment.objects.filter(comment_id = text_id).order_by('create_date')
    content = {'text_list':text_list,
               'comment_list':comment_list,
               'text_id': text_id}
    return render(request, 'board/detail.html', content)

def create(request):
    if request.method == "POST":
       create = Create()
       create.title = request.POST['ftitle']
       create.contents = request.POST['fcontents']
       create.author = request.POST['fauthor']
       create.save()  
       return redirect(f'/NoticeBoard/{create.id}')
   
    else:
        return render(request, 'board/create.html')
    
def update(request, text_id):
    text_list = get_object_or_404(Create, pk=text_id)
    if request.method == "GET":
        content={'text_list':text_list,
                'text_id':text_id}
        return render(request, 'board/update.html', content)
    
    else:
        text_list.title = request.POST['ftitle']
        text_list.contents = request.POST['fcontents']
        text_list.author = request.POST['fauthor']
        text_list.save()
        return redirect(f'/NoticeBoard/{text_id}')
    
def delete(request, text_id):
    delete_notice = get_object_or_404(Create, pk=text_id)
    delete_notice.delete()
    return redirect('/NoticeBoard')

def comment_create(request, text_id):
    content={'text_id':text_id}

    if request.method == "POST":
        create_instance = get_object_or_404(Create, pk=text_id)
        new_comment = Comment.objects.create(comment_id=create_instance, contents=request.POST['fcomment'])
        return redirect(f'/NoticeBoard/{text_id}')

    else:
        return render(request, 'board/detail.html',content)
