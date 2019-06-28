from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, View

from utils.email_send import send_register_email

from .forms import LoginForm, RegisterForm
from .models import UserProfile, EmailVerifyRecord


# Create your views here.


# 首页
class IndexView(TemplateView):
    template_name = 'index.html'


# 支持邮箱登录
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(
                Q(username=username) | Q(email=username))
            print(user, password, user.check_password(password))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 登录
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST['username']
            pass_word = request.POST['password']
            user = authenticate(request,
                                username=user_name,
                                password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html', {})
                else:
                    return render(request, 'login.html', {'msg': '用户名未激活！'})
            else:

                return render(request, 'login.html', {'msg': '用户名或者密码错误！'})
        else:
            return render(request, 'login.html', {'login_form': login_form})


# 注册
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST['email']
            pass_word = request.POST['password']
            # password = make_password(pass_word)
            user_profile = UserProfile.objects.create_user(username=user_name, email=user_name, password=pass_word)
            user_profile.is_active = False
            user_profile.save()
            # 发送注册邮件
            send_register_email(user_name, 'register')
            return render(request, 'login.html', {})


# 激活账户
class ActiveUserView(View):
    def get(self, request, active_code):
        record = EmailVerifyRecord.objects.filter(code=active_code)
        if record:
            for i in record:
                record_email = i.email
                user_profile = UserProfile.objects.get(email=record_email)
                user_profile.is_active = True
                user_profile.save()
        return render(request, 'login.html', {})
