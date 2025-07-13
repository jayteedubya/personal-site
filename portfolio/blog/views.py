from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader

from .models import BlogPost, Comment

# Create your views here.
def blog_home(request: HttpRequest) -> HttpResponse:
    posts = BlogPost.objects.all()
    template = loader.get_template("blog/index.html")
    context = {
        "posts": posts
    }
    return HttpResponse(template.render(context, request))


def blog_post_detail(request: HttpRequest, post_id: int) -> HttpResponse:
    post = BlogPost.objects.get(id=post_id)
    template = loader.get_template("blog/post_detail.html")
    context = {
        "post": post
    }
    return HttpResponse(template.render(context, request))
