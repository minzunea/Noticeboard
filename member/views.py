from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import auth

# Create your views here.
def index(request):
    return HttpResponse("로그인 앱 view_index")

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(
                request=request,
                username=username,
                password=password
            )
            if user is not None:
                auth.login(request, user)
                return redirect('/NoticeBoard')
        
        return redirect('member:login')
    
    else:
        form = AuthenticationForm()
        context = {'form' : form}
        return render(request, 'member/login.html', context)
    
def logout(request):
   auth.logout(request)
   return redirect('/NoticeBoard')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect('/NoticeBoard')
        return redirect('member:signup')
    
    else:
        form = UserCreationForm()
        context = {'form' : form}
        return render(request, 'member/signup.html', context)