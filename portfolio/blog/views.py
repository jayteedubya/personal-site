from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .models import BlogPost, Comment

# Create your views here.
def blog_home(request: HttpRequest) -> HttpResponse:
    posts = BlogPost.objects.all()
    return HttpResponse("\n".join(map(lambda post: f"<h2>{post.title}</h2>", posts)))


def blog_post_detail(request: HttpRequest, post_id: int) -> HttpResponse:
    post = BlogPost.objects.get(id=post_id)
    return HttpResponse(f"Details of blog post: {post.title}")
