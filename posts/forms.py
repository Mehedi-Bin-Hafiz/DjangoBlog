from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields=[ 'title', 'content']

        widgets={
            'title' : forms.TextInput(
            attrs={
                "class": "form-control", "placeholder": "enter fullname", "id": "form_full_name",
            }),

        'content' : forms.Textarea(
            attrs={
                "class": "form-control", "placeholder": "enter content", "id": "form_full_content",
            })
        }

