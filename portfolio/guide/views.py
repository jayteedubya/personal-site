from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def guide_home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Welcome to the guide Home Page")
