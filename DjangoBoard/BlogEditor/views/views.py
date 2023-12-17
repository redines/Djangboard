from django.shortcuts import render, redirect
from ..models import Post
from ..forms.forms import EditForm

def home(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "BlogEditorhome.html",context)

def edithome(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditForm(request.POST, instance=post)
        if form.is_valid():
            
           form.save()
           return redirect('blog_home')
    else:
        form = EditForm(instance=post)
    
    context = {
            "post": post,
            "form": form
        }

    return render(request, 'blogedit.html', context)