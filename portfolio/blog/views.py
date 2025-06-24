from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def blog_home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Welcome to the Blog Home Page")
