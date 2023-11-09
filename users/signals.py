from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


#Make receiver function to receive signal when user is created and create profile for user
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


#Make receiver function to receive signal when user is saved and save profile for user
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()