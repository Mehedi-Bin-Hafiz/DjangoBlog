from django import forms
from .models import Post

class ContactForm(forms.ModelForm):
    class Meta:
        model = Post

        fields=[
            fullname = forms.CharField(widget=forms.TextInput(
            attrs={
                "class": "form-control", "placeholder": "enter fullname", "id": "form_full_name",
            })
        )

        # here fullname act as name in html
        email = forms.EmailField(widget=forms.EmailInput(
            attrs={
                "class": "form-control", "placeholder": "enter email", "id": "form_full_email",
            }))

        content = forms.CharField(widget=forms.Textarea(
            attrs={
                "class": "form-control", "placeholder": "enter content", "id": "form_full_content",
            }))

        ]

