"""为应用程序users定义URL模式"""

from django.urls import path, re_path
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
  # 登陆界面
  path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
  
  # 注销页面
  # path('logout/', views.logout_view, name='logout'),
  path('logout', LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),


  # 注册页面
  path('register/', views.register, name='register'),

]

