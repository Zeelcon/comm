from django.shortcuts import render, redirect

from django.http import HttpResponse, request
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

#account-注册-登录-忘记密码
def register(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.clean_data.get('username')
                messages.success(request, 'Account was created for' + user)

                return redirect

        context = {'form':form}
        return render(request, 'account/register_page.html', context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('home_page')
            else:
                messages.info(request, 'Username Or password is wrong!')

        context = {}
        return render(request, 'account/login_page.html', context)

def logoutUser():
    logout(request)
    return redirect('login_page')

def forget(request):
    context = {}
    return render(request, 'account/forget_page.html', context)

# @login_required(login_url='login_page')
#blog-首页-用户信息-文章
def home(request):
    context = {}
    return render(request, 'commusic/home_page.html', context)

# @login_required(login_url='login_page')
def users(request):
    context = {}
    return render(request, 'commusic/users_page.html', context)

# @login_required(login_url='login_page')
def article(request):
    context = {}
    return render(request, 'commusic/article_page.html', context)