from django.contrib import admin
from .models import Profile

admin.site.register(Profile) #Registering models w/ admin page, so they may be viewd/editted there.
