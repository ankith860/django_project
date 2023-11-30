from django.db import models
from django.contrib.auth.models import User
from PIL import Image #pillow
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.conf import settings




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #One To One relationship: 1 Profile belongs to 1 User and vice versa
    #Cascade deletion deletes the Profile if the User is deleted, but not vice versa.
    username = models.TextField(default='user', max_length=100)
    email = models.EmailField(default='email@email.com')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f"{self.user.username} Profile" #Query of Profile instance yields a human readable string
    
    # def save(self, *args, **kwargs): #overriding parent class save method
    #     super().save(*args, **kwargs) #runs parent class save method
    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300: #resize saved image if larger than 300x300 pixels
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)




#Receiver function to create an authorization token for User when User instance is created 
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)