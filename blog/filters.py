import django_filters
from django_filters import CharFilter
from .models import * #importing all models in current model directory

class PostFilter(django_filters.FilterSet):
    content = CharFilter(field_name='content', lookup_expr='icontains')
    title = CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Post
        fields = '__all__' #filters to allow all fields

