#from django.forms.models import BaseModelForm
#from django.http import HttpResponse
#from typing import Any
#from django.db import models
from django.urls import reverse
#from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentCreationForm
from django.contrib.auth.models import User
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .filters import PostFilter
import requests


'''
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
'''




def APIPostListView(request):
    response = requests.get('http://127.0.0.1:8000/api/posts/').json()
    return render(request, 'blog/api.html', {'response': response})




class PostListView(ListView): 
    model = Post 
    template_name = 'blog/home.html'
    context_object_name = 'posts' #Renaming variable per django conventions so it works with our blog home template as is
    ordering = ['-date_posted']
    paginate_by = 4
    
    def get_queryset(self):
        filter = PostFilter(self.request.GET, queryset=Post.objects.all().order_by('-date_posted'))
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter = PostFilter(self.request.GET, queryset=Post.objects.all().order_by('-date_posted'))
        context["filter"] = filter
        return context
    



'''
def search_view(request):

    if request.method == "GET":

        query=request.GET.get('q')
        posts = Post.objects.filter(title__contains=query)
        template="blog/search/results-view.html"

        context = {
            "query":query,
            "posts": posts
        }      

        if request.htmx:
            template = "blog/search/partials/results.html"
            return render(request, template, context)
        
        return render(request, template, context)
'''




class UserPostListView(ListView): 
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5
    ordering = ['-date_posted']

    def get_queryset(self): #modify/override query_set that this view returns
        
        user = get_object_or_404(User, username=self.kwargs.get('username')) #Get username from url using shortcut 'get_object_or_404'. Variables sent in are stored as kwargs and accessed by instance of class-view via self

        return Post.objects.filter(user=user).order_by('-date_posted') #Ordering was overriden, fixing ordering in return statement




class PostDetailView(DetailView): #Made this one strictly with django default conventions, for use with details of a single post
    model = Post 




class PostCreateView(LoginRequiredMixin, CreateView): 
    '''Form-Based View that inherits from create view (the form) and login mixin which is like a class-based decorator that makes this view avaialble only if logged in'''
    model = Post 
    fields = ['title', 'content'] 

    def form_valid(self, form): #Set author to current logged in user when submitting, before parent class' form_valid method is run and checks the form. 
        form.instance.author = self.request.user.username
        form.instance.user = self.request.user
        form.instance.image_url = self.request.user.profile.image.url

        return super().form_valid(form) #runs parent class method




class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  #Form-Based View, uses same template as create view
    model = Post 
    fields = ['title', 'content'] 
    
    def form_valid(self, form): #setting author again/ also checking 
        form.instance.user = self.get_object().user
        return super().form_valid(form) #built in save method
    
    def test_func(self): #UserPassesTestMixin Will run this
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False




class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  
    model = Post 
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False




def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})




class CommentCreateView(LoginRequiredMixin, CreateView):
    success_url = '/' 
    model = Comment 
    form_class = CommentCreationForm
    template_name='blog/add_comment.html'

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.user = self.request.user
        form.instance.author = self.request.user.username
        return super().form_valid(form)





class CommentDeleteView(LoginRequiredMixin, DeleteView): 
    model = Comment
    template_name='blog/delete_comment.html'

    def get_success_url(self):
        comment = Comment.objects.get(id=self.kwargs['pk'])
        return reverse('post-detail', kwargs= {'pk': comment.post_id})




class UserCommentListView(ListView): #View for an object we will be looping over to display, this must be provided
    model = Comment
    template_name = 'blog/user_comments.html'
    context_object_name = 'comments'
    paginate_by = 10

    def get_queryset(self):
        user=self.request.user 
        return Comment.objects.filter(user=user).order_by('-date_posted')




class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  #Form-Based View, uses same template as create view
    model = Comment 
    fields = ['content'] 
    template_name= 'blog/update_comment.html'
    
    def form_valid(self, form): #setting author again/ also checking 
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self): #UserPassesTestMixin Will run this
        comment = self.get_object()
        if self.request.user == comment.user:
            return True
        return False
    
    def get_success_url(self):
        comment = Comment.objects.get(id=self.kwargs['pk'])
        return reverse('post-detail', kwargs= {'pk': comment.post_id})