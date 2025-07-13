from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_home, name="blog_home"),
    path("<int:post_id>/", views.blog_post_detail, name="blog_post_detail"),
]
