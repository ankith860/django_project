from django.db import models
from django.contrib.auth.models import User
from PIL import Image #pillow


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    # One to One relationship, users have 1 pofile picture, 1 profile and profile picture belongs to 1 user
    # Cascade deletion deletes the profile if the User is deleted, but not vice versa.
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') #store locally

    def __str__(self):
        return f"{self.user.username} Profile"
    
    def save(self): #overriding parent class save method with our own functionality
        super().save() #runs parent class save method
        # grab and resize saved image
        
        img = Image.open(self.image.path) #opens/store current instance's image

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)