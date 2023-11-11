from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
import requests

def register(request):
    '''
    - when the register page is called, the httprequest method is get the first time
    - the form is passed to the template and rendered
    - upon submitting the form, you send a post method request to this url, this function is run and you are redirected to the blog home if the post data is valid. The register page is not rendered.
    '''

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid(): 
           #if the code isn't valid, the else: code block is ingored goes to final return statement
           form.save()
           username = form.cleaned_data.get('username')
           messages.success(request, f"You're account has been created! You are now able to login, {username}.")
           return redirect('login')
           #this is run and the second return statement is ignored
    else:
      form = UserRegisterForm()
      #runs if form method is Get not Post
    return render(request, 'users/register.html', {'form': form})


'''
message.debug
message.success
message.error
message.warning
message.info
'''

@login_required
def profile(request):
   if request.method == 'POST':
    u_form = UserUpdateForm(request.POST, instance=request.user) # form instance from current user that is fed in POST data
    p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) #same as ^ but for image, post data comes with file data!

    if u_form.is_valid() and p_form.is_valid():
       u_form.save()
       p_form.save()
       messages.success(request, f"You're account has been updated!")
       return redirect('profile')

   else:
    u_form = UserUpdateForm(instance=request.user) # form instance that's populated  with username and email of current user
    p_form = ProfileUpdateForm(instance=request.user.profile) #same as ^ but for image
   context = {'u_form': u_form, 'p_form': p_form}

   return render(request, 'users/profile.html', context)



