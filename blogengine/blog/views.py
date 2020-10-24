"""docs"""
from django.shortcuts import render
from . models import Post 


def posts_list(request):
    """docstring"""
    posts = Post.objects.all()
    return render(request, 'blog/posts_list.html', context={'posts': posts})

def post_detail(request, slug):
    """post detail"""
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post': post})