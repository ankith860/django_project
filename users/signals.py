from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile




#Receiver function to create user profile when user instance is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, username=instance.username, email=instance.email)




#Receiver function to save user profile when user instance is saved 
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()



#Receiver function to delete user instance when user profile is deleted
@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    instance.user.delete()