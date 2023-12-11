from django.shortcuts import render
from ..models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "BlogEditorhome.html",context)