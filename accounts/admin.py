from django.contrib import admin

from .models import CustomUser

# ユーザーの情報を管理画面で確認できるように
admin.site.register(CustomUser)