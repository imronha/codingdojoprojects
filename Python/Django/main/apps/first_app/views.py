from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)

def test(request):
    response = "Hello, I am test"
    return HttpResponse(response)
