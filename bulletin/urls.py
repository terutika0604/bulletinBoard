from django.urls import path
from . import views

app_name = 'bulletin'
urlpatterns = [
    # TOPページ
    # path('index/', views.IndexView.as_view(), name='index'),

    # 記事一覧ページ
    # path('bulletin/list/', views.BulletinListView.as_view(), name='bulletin_list'),
    path('', views.IndexView.as_view(), name='index'),

    # 記事作成ページ
    path('bulletin/create/', views.BulletinCreateView.as_view(), name='bulletin_create'),

    # 記事作成完了ページ
    path('bulletin/create/complete/', views.BulletinCreateCompleteView.as_view(), name='bulletin_create_complete'),


    # 記事詳細ページ
    path('bulletin/detail/<int:pk>/', views.BulletinDetailView.as_view(), name='bulletin_detail'),

    # コメント投稿用
    path('bulletin/create/<int:pk>/', views.CommentCreate.as_view(), name='comment_create'),
]