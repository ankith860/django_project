''' Inheriting and customizing user creation/update and profile update form classes '''


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile




class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #Add email field to inherited user creation form 
    
    class Meta: #Meta class allows modification of form fields via specified Model
        model = User
        fields = ['username', 'email', 'password1', 'password2'] #password2 is the repeated password




class UserUpdateForm(forms.ModelForm): #Customize form to update user model's username and email fields
    email = forms.EmailField() #Adds Email Field to the inherited form
    
    class Meta:
        model = User
        fields = ['username', 'email']




class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']