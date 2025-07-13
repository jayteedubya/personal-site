from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import BlogPost, Comment

# Create your views here.
def blog_home(request: HttpRequest) -> HttpResponse:
    posts = BlogPost.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "blog/index.html", context)


def blog_post_detail(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(BlogPost, id=post_id)
    comments = list(Comment.objects.filter(post=post_id).order_by('-created_at').all())
    context: dict[str, BlogPost | list[Comment]] = {
        "post": post,
        "comments": comments
    }
    return render(request, "blog/post_detail.html", context)
