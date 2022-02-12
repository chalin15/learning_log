from django.shortcuts import render, redirect

# Create your views here.

from django.urls import path, re_path
from django.http import HttpResponseRedirect
from django.urls.resolvers import URLResolver, get_resolver
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login,redirect_to_login
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt

from . import views

def logout_view(request):
  """注销用户"""
  # LogoutView.logout_then_login(request)
  redirect_to_login(request, 'learning_logs:index.html')
  # LogoutView.as_view()
  # return HttpResponseRedirect(URLResolver('', 'learning_logs:index'))

@csrf_exempt
def register(request):
  """注册用户"""
  if request.method != 'POST':
    # 显示空的注册表单
    form = UserCreationForm()
  else:
    # 处理填写好的表单
    form = UserCreationForm(data=request.POST)
    
    if form.is_valid():
      new_user = form.save()
      # 让用户自助登录，再重定向到主页
      authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
      print('here is asset')

      login(request, authenticated_user)
      return redirect('learning_logs/index')
      # return HttpResponseRedirect(get_resolver('learning_logs:index'))
      
  context = {'form': form}
  return render(request, 'users/register.html', context)
