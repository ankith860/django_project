from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),

    #path('search/', search_view, name='search'),

    path('apihome/', views.APIPostListView, name='api-home'),

    path('user/<str:username>/', UserPostListView.as_view(), name='user-post'),
    path('post/new/', PostCreateView.as_view(), name='post-create'), 
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), 
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),#same template as create view
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),

    path('post/<int:pk>/comment_create/', CommentCreateView.as_view(), name='comment-create'),
    path('post/comment/<int:pk>/delete', CommentDeleteView.as_view(), name='comment-delete'),
    path('mycomments/', UserCommentListView.as_view(), name='user-comments'),
    path('post/comment/<int:pk>/update', CommentUpdateView.as_view(), name='comment-update'),
]