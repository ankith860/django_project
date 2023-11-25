''' Convert complex data types from database, for example, to python objects for easy manipulation. Can then render them as JSON for universal transportion/parsing/access.'''

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

