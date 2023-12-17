from django import forms
from ..models import Post

class EditForm(forms.ModelForm):
    categories = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
           attrs={"class": "form-control"}
        )
    )

    body = forms.CharField(
        widget=forms.Textarea(
        attrs={"class": "form-control"}
        )
    )

    class Meta:
        model = Post
        fields = ['categories', 'body']