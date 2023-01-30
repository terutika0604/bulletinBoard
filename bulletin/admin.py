from django.contrib import admin
from .models import Bulletin, Comment

# Bulletinの情報を管理画面で確認できるように
admin.site.register(Bulletin)

# Commentの情報を管理画面で確認できるように
admin.site.register(Comment)