from django.shortcuts import render
from .models import Post

def post_list(request):
    projects = Post.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "portfolio/post_list.html", context)