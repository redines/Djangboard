from django.shortcuts import render
from ..models import Post
from django.http import HttpResponseRedirect
from ..forms.forms import EditForm

def blogedit(request, pk):
    post = Post.objects.get(pk=pk)
    form = EditForm()

    if request.method == "POST":
        form = EditForm(request.POST)
        if form.is_valid():
            content = EditForm(
                category=form.cleaned_data["category"],
                body=form.cleaned_data["body"],
                post=post,
            )
            content.save()
            return HttpResponseRedirect(request.path_info)
        
    context = {
        "post": post,
        "form": EditForm,
    }

    return render(request, "blogedit.html", context)