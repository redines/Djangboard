from django import forms

class EditForm():
    category = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control"}
        )
    )