from django.shortcuts import render, redirect
from ..models import Post
from django.http import HttpResponseRedirect
from ..forms.forms import EditForm
from django.views.decorators.csrf import csrf_exempt

def blogedit(request, pk):
    post = Post.objects.get(pk=pk)
        
    context = {
        "post": post
    }

    return render(request, "blogedit.html", context)

def blogupdate(request, pk):
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
            return HttpResponseRedirect('')
        
    context = {
        "post": post,
        "form": EditForm()
    }

    return render(request, "blogedit.html", context)

@csrf_exempt
def update(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method != 'POST':
            content = EditForm(
                category=EditForm.cleaned_data["category"],
                body=EditForm.cleaned_data["body"],
                post=post,
            )
            content.save()
            return HttpResponseRedirect('')

    else:
        form = EditForm(instance=post, data=request.POST) 
        if form.is_valid():
            form.save()
            return redirect('blogs/edit_post.html', post_id=post.id)


    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)