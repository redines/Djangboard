from django import forms

class EditForm(forms.Form):
    category = forms.CharField(
        max_length=60,
        #widget=forms.TextInput(
         #   attrs={"class": "form-control", "placeholder": "Edit category"}
        #)
    )

    body = forms.CharField(
       # widget=forms.Textarea(
        #    attrs={"class": "form-control", "placeholder": "Edit blog post"}
        #)
    )