import django_filters
from django_filters import CharFilter, DateFilter
from django.forms.widgets import TextInput
from .models import * #importing all models in current model directory

class PostFilter(django_filters.FilterSet):
    content = CharFilter(field_name='content', lookup_expr='icontains')
    title = CharFilter(field_name='title', lookup_expr='icontains')
    author = CharFilter(field_name='author', label ='Author', lookup_expr='icontains')
    start_date = DateFilter(field_name='date_posted', label ='Date Posted Start Range', lookup_expr='gte', widget=TextInput(attrs={'placeholder': 'MM/DD/YY'}))
    end_date = DateFilter(field_name='date_posted', label ='Date Posted End Range', lookup_expr='lte', widget=TextInput(attrs={'placeholder': 'MM/DD/YY'}))
    
    class Meta:
        model = Post
        fields = '__all__' #filters to allow all fields
        exclude = ['image_url', 'user', 'date_posted']
