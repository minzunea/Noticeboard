from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Create, Comment


def index(request):
    text_list = Create.objects.order_by('create_date')
    content = {'text_list':text_list,}
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
       create.text_title = request.POST['ftitle']
       create.text_body = request.POST['ftext_body']
       create.creater = request.POST['fcreater']
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
        text_list.text_title = request.POST['ftitle']
        text_list.text_body = request.POST['ftext_body']
        text_list.creater = request.POST['fcreater']
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
        new_comment = Comment.objects.create(comment_id=create_instance, comment_text=request.POST['fcomment'])
        new_comment.save()
        return redirect(f'/NoticeBoard/{text_id}')

    else:
        return render(request, 'board/detail.html',content)
