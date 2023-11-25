'''URL ROUTES TO CONSUME API, STILL IN DEVELOPMENT PHASE'''

from django.urls import path
from . import views
from .views import *


urlpatterns =[
  path('profile/', ProfileView.as_view(), name = 'api-profile'),
  path('posts/', AllPostListView.as_view(), name = 'api-all-posts'),
  path('myposts/', PostListView.as_view(), name = 'api-posts'),
  path('myposts/<int:id>/', PostDetailView.as_view(), name = 'api-post-detail'),
]
