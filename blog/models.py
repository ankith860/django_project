from django.db import models
from django.utils import timezone, dateformat
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  date_posted = models.CharField(default=str(dateformat.format(timezone.now(), 'Y-m-d H:i')), max_length=70) 
  user = models.ForeignKey(User, on_delete = models.CASCADE) #this just relates the User model to the author field, but it doesn't get the currently logged in user.
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
  date_posted = models.CharField(default=str(dateformat.format(timezone.now(), 'Y-m-d H:i')), max_length=70) 
  
  def __str__(self):
    return "%s commented on %s's post '%s'" %(self.user.username, self.post.author, self.post.title)