from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  date_posted = models.DateTimeField(default=timezone.now) #dont put parenthises after timezone.now so its passed but not called
  author = models.ForeignKey(User, on_delete = models.CASCADE) #this just relates the User model to the author field, but it doesn't get the currently logged in user.

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('post-detail', kwargs={'pk': self.pk}) #returns full path as a string


