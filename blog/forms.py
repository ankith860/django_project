from django import forms
from .models import Comment

class CommentCreationForm(forms.ModelForm):
    #Not adding a field
    class Meta:
        model = Comment #Model You want to work with/customize
        fields = ['content'] #Fields You want to work with/customize

        widget = {
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }