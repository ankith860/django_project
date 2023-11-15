from django.urls import path
from . import views
from .views import APIPostListView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, CommentCreateView, CommentDeleteView, UserCommentListView, CommentUpdateView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('apihome/', views.APIPostListView, name='api-home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'), 
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), 
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'), #uses same template as create view
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-post'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/comment_create/', CommentCreateView.as_view(), name='comment-create'),
    path('post/comment/<int:pk>/delete', CommentDeleteView.as_view(), name='comment-delete'),
    path('mycomments/', UserCommentListView.as_view(), name='user-comments'),
    path('post/comment/<int:pk>/update', CommentUpdateView.as_view(), name='comment-update'),
]