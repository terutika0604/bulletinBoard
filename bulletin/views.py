from .models import Bulletin, Comment
from .forms import BulletinForm, CommentForm
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# TOPページ
class IndexView(ListView):
    template_name = 'index.html'
    model = Bulletin

# 記事作成ページ
# 未ログインユーザーからのアクセス禁止LoginRequiredMixin
class BulletinCreateView(LoginRequiredMixin, CreateView):
    template_name = 'bulletin_create.html'
    # フォームと紐づけ
    form_class = BulletinForm
    # submit後の行き先
    success_url = reverse_lazy('bulletin:bulletin_create_complete')

    # ログインユーザーをTemplateに渡す
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

# 記事作成完了ページ
class BulletinCreateCompleteView(LoginRequiredMixin,TemplateView):
    template_name = 'bulletin_create_complete.html'

# 記事詳細ページ
class BulletinDetailView(DetailView):
    template_name = 'bulletin_detail.html'
    model = Bulletin

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # テンプレートにコメント作成フォームを渡す
        context['comment_form'] = CommentForm

        return context

# 記事へのコメント作成ビュー
# ページは表示されないが、コメントを作成するために使用
class CommentCreate(CreateView):
    # Commentモデル,Comment作成フォームと連携
    model = Comment
    form_class = CommentForm

    # 渡されたpkからbulletinを探してきてそのidをCommentの外部キーに設定する
    def form_valid(self, form):
        post_pk = self.kwargs.get('pk')
        post = get_object_or_404(Bulletin, pk=post_pk)

        comment = form.save(commit=False)
        comment.bulletin = post
        comment.save()

        # 記事詳細にリダイレクト
        return redirect('bulletin:bulletin_detail', pk=post_pk)