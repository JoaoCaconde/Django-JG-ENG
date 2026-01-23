from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    projects = Post.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "portfolio/post_list.html", context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    project = Post.objects.get(pk=pk)
    context = {
        "project": project
    }
    return render(request, "portfolio/post_detail.html", context)