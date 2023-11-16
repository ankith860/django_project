import django_filters
from django_filters import CharFilter, DateFilter
from django.forms.widgets import TextInput
from .models import * #importing all models in current model directory

class PostFilter(django_filters.FilterSet):

    content = CharFilter(field_name='content', lookup_expr='icontains',label=False, widget=TextInput(attrs={'placeholder': 'content contains:', 'size': 30}))

    title = CharFilter(field_name='title', lookup_expr='icontains',label=False, widget=TextInput(attrs={'placeholder': 'title contains:', 'size': 30}))

    author = CharFilter(field_name='author', lookup_expr='icontains',label=False, widget=TextInput(attrs={'placeholder': 'author contains:', 'size': 30}))

    start_date = DateFilter(field_name='date_posted', label =False, lookup_expr='gte', widget=TextInput(attrs={'placeholder': 'Posted On/After MM/DD/YY', 'size': 30}))

    end_date = DateFilter(field_name='date_posted', label=False, lookup_expr='lte', widget=TextInput(attrs={'placeholder': 'Posted On/Before MM/DD/YY', 'size': 30}))
    
    class Meta:
        model = Post
        fields = '__all__' #filters to allow all fields
        exclude = ['image_url', 'user', 'date_posted']
