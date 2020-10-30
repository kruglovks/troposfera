from django.shortcuts import render, redirect, get_object_or_404, reverse
from . models import Post, Tag
from . forms import TagForm, PostForm
from django.views.generic import View
from . utils import DetailObjectMixin, CreateObjectMixin, UpdateObjectMixin, DeleteObjectMixin



def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts_list.html', context={'posts': posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})



class PostDetail(DetailObjectMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagDetail(DetailObjectMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'



class TagCreate(CreateObjectMixin, View):
    model = TagForm
    template = 'blog/tag_create.html'


class PostCreate(CreateObjectMixin, View):
    model = PostForm
    template = 'blog/post_create.html'



class TagUpdate(UpdateObjectMixin, View):
    model = Tag
    form_class = TagForm
    template = 'blog/tag_update.html'


class PostUpdate(UpdateObjectMixin, View):
    model = Post
    form_class = PostForm
    template = 'blog/post_update.html'


class TagDelete(DeleteObjectMixin, View):
    model = Tag
    template = 'blog/tag_delete.html'
    redirect_url = 'tags_list_url'


class PostDelete(DeleteObjectMixin, View):
    model = Post
    template = 'blog/post_delete.html'
    redirect_url = 'posts_list_url'