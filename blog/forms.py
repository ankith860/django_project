from django import forms
from .models import Comment


class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content'] #Fields You want to work with/customize
        widget = {'content': forms.Textarea(attrs={'class': 'form-control'})}