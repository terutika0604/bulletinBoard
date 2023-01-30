from django import forms
from .models import Bulletin, Comment

# フォームを定義
class BulletinForm(forms.ModelForm):
    class Meta:
      # モデルと紐づけ
        model = Bulletin
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
    class Meta:
      # モデルと紐づけ
        model = Comment
        fields = ('comment_user', 'comment_text',)