from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def home(req):
    return HttpResponse('<h1>Hello World</h1>')