"""Commusic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from community import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #注册-登录-忘记密码
    path('register', views.register, name='register_page'),
    path('login', views.loginUser, name='login_page'),
    path('logout', views.logoutUser, name='logout_page'),
    path('forget', views.forget, name='forget_page'),
    #首页-文章-用户信息
    path('', views.home, name='home_page'),
    path('article', views.article, name='article_page'),
    path('users', views.users, name='users_page'),


]
