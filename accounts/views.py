from django.shortcuts import render
from .forms import LoginForm, SignupForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

class LoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm

class LogoutView(LogoutView):
    template_name = 'logout.html'

class SignupView(CreateView):
    template_name = 'signup.html'
    form_class = SignupForm
    success_url = '/bulletin/create/'

    # フォームから送信されてきたデータが妥当である際にはデータベースにレコードを保存するだけでなく（つまりユーザーアカウント登録を行うだけでなく）、ログインまで実行させる
    def form_valid(self, form):
        result = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return result