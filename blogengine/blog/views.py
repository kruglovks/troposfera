from django.shortcuts import render, redirect
from . models import Post, Tag
from . forms import TagForm
from django.views.generic import View
from . utils import DetailObjectMixin

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



class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        
        return render(request, 'blog/tag_create.html', context={'form': bound_form})
