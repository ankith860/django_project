#from django.forms.models import BaseModelForm
#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView #Class-Based Views
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
    paginate_by = 5
    
    '''def get_queryset(self):
        filter = PostFilter(self.request.GET, queryset=Post.objects.all())
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter = PostFilter(self.request.GET, queryset=Post.objects.all())
        context["filter"] = filter
        return context'''



class UserPostListView(ListView): #View for an object we will be looping over to display, this must be provided
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self): #modify/override query_set that this view returns
        user = get_object_or_404(User, username=self.kwargs.get('username')) #get username from url using shortcut 'get_object_or_404'. variables sent in are stored as kwargs and accessed by instance of class-view via self
        return Post.objects.filter(user=user).order_by('-date_posted') #ordering was also overriden, so we add proper ordering in return here


class PostDetailView(DetailView): #Made this one strictly with django default conventions, did not rename varibles or paths. Will render details of a single-post when post-link is clicked or path is accessed for single post
    model = Post 



class PostCreateView(LoginRequiredMixin, CreateView): #Form-Based View that inherits from create view (the form) and login mixin which is like a class-based decorator that makes this view avaialble only if logged in 
    model = Post 
    fields = ['title', 'content'] #This is how you add fields in a class-based view that makes a form, not a regular form

    def form_valid(self, form): #Set author to current logged in user when submitting, before parent class' form_valid method is run and checks the form. 
        form.instance.author = self.request.user.username
        form.instance.user = self.request.user
        form.instance.image_url = self.request.user.profile.image.url

        return super().form_valid(form) #runs parent class method



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  #Form-Based View, uses same template as create view
    model = Post 
    fields = ['title', 'content'] 
    
    def form_valid(self, form): #setting author again/ also checking 
        form.instance.user = self.get_object().author
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