from django.shortcuts import render
from .models import Blog


def blog(request):
    obj1 = Blog.objects.all()
    return render(request, 'blog.html', {'ob': obj1})
