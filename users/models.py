from django.db import models
from django.contrib.auth.models import User
from PIL import Image #pillow
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.TextField(default='user', max_length=100)
    email = models.EmailField(default='email@email.com')
    # One to One relationship, users have 1 pofile picture, 1 profile and profile picture belongs to 1 user
    # Cascade deletion deletes the profile if the User is deleted, but not vice versa.
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') #store locally

    def __str__(self):
        return f"{self.user.username} Profile"
    
    def save(self, *args, **kwargs): #overriding parent class save method with our own functionality
        super().save(*args, **kwargs) #runs parent class save method
        # grab and resize saved image
        
        img = Image.open(self.image.path) #opens/store current instance's image

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)