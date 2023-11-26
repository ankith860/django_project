from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
import requests




def register(request):
  ''' When the register page is initially accessed, the HTTP request method is GET. The form is passed to the users/register.html template and rendered. Upon submitting the form, the user sends a HTTP POST request to the register page. This function's conditional for POST methods is run, the form is cleaned and user data is saved if it passes validation. The user is then redirected to the login page, and a 'success' message is displayed. If the user's input is not valid, the user is redirected to the register page with their inputted data still filled in, but an error message is displayed. '''

  if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid(): 
          form.save()
          username = form.cleaned_data.get('username')
          messages.success(request, f"You're account has been created! You are now able to login, {username}.")
          return redirect('login')
  else:
    form = UserRegisterForm()

  return render(request, 'users/register.html', {'form': form})




@login_required
def profile(request):
   if request.method == 'POST':
    u_form = UserUpdateForm(request.POST, instance=request.user) #form instance from current user POSTed
    p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) 
    if u_form.is_valid() and p_form.is_valid():
       u_form.save()
       p_form.save()
       messages.success(request, f"You're account has been updated!")
       return redirect('profile')
   else:
    u_form = UserUpdateForm(instance=request.user) #form populated w/ current user's username & email
    p_form = ProfileUpdateForm(instance=request.user.profile)
   
   context = {'u_form': u_form, 'p_form': p_form}

   return render(request, 'users/profile.html', context)




@login_required
def delete_profile(request, pk):
  queryset = User.objects.get(id=pk)

  if request.method == 'POST':
    queryset.delete()
    messages.info(request, f"You're account has been deleted. Hope you come back!")
    return redirect('register')

  return render(request, 'users/profile_delete_confirm.html')