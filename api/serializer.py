from rest_framework import serializers
from users.models import Profile
from blog.models import Post

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = '__all__'