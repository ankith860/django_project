from django.db import models
import datetime
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
  '''Post model's user has many to one relationship with user model via foreign key; thus, a post only has one user but one user can have many posts.''' 

  title = models.CharField(max_length=100)
  content = models.TextField()
  date_posted = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User, on_delete = models.CASCADE) #Currently logged in user provided via post creation view/template.
  author = models.TextField(default='user', max_length=100)
  image_url = models.URLField(max_length=300)

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('post-detail', kwargs={'pk': self.pk}) #returns full path as a string




class Comment(models.Model):
  post = models.ForeignKey(Post, related_name="comments", on_delete = models.CASCADE)
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  author = models.CharField(max_length=100)
  content = models.TextField(max_length=500)
  date_posted = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return "%s commented on %s's post '%s'" %(self.user.username, self.post.author, self.post.title)