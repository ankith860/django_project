from django.urls import path
from . import views
from .views import APIPostListView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('apihome/', views.APIPostListView, name='api-home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'), 
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), 
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'), #uses same template as create view
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-post'),
    path('about/', views.about, name='blog-about'),
]


'''
.as_view() 'converts' class-based view to an actual view

<pk> is the primary key of post variable, an integer. This is what DetailView expects by default. It is passed into the path when the button is clicked and the right view is called. The home.html template thus handles this in the url tag
'''