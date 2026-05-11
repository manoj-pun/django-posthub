from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'description']
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Write a description for your post...'
            }),
            'image': forms.FileInput(attrs={
                'accept': 'image/*'
            })
        }

        