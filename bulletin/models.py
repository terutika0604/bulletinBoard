from django.db import models
from django.utils import timezone

# 記事の情報を管理するモデル
class Bulletin(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=40)
    text = models.CharField(verbose_name='本文', max_length=200)
    created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)

    # 管理画面でタイトルが表示されるため見やすくなる
    def __str__(self):
        return self.title

# コメントの情報を管理するモデル
class Comment(models.Model):
    bulletin = models.ForeignKey(Bulletin, on_delete=models.CASCADE)
    comment_user = models.CharField(verbose_name='ユーザー名', max_length=40)
    comment_text = models.CharField(verbose_name='コメント', max_length=200)
    created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)

    def __str__(self):
        return self.comment_user