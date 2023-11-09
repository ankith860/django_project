#This is not a template, we just wanted to inherit the user creation form class and make our own custom form class.

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #Add email field to inherited user creation form 
    
    class Meta: # Through some process, a meta class allows you to modify how class is created/structured
        model = User #Model to work with and take fields from
        fields = ['username', 'email', 'password1', 'password2'] #Fields displayed on form
        #password1 is actual password, password2 is the repeated password



class UserUpdateForm(forms.ModelForm): #Update user model's username and email
    email = forms.EmailField() #Adds Email Field to the inherited form
    
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    #Not adding a field
    class Meta:
        model = Profile #Model You want to work with/customize
        fields = ['image'] #Fields You want to work with/customize