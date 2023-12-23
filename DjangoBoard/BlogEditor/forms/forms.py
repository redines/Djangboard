from django import forms
from ..models import Post,Category

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['categories', 'body']

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "type":"checkbox" 
            }
        )
    )

    body = forms.CharField(
        widget=forms.Textarea(
        attrs={
            "style": "resize: none;",
            "class": "form-control",}
        )
    )

