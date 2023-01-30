from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# ユーザー登録用フォーム
class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

# ログイン用フォーム
class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email']