from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    placeholder = "Placeholder to later display all the list of users"
    return HttpResponse(placeholder)

def register(request):
    placeholder = "Placeholder for users to create a new user record"
    return HttpResponse(placeholder)

def login(request):
    placeholder = "Placeholder for users login"
    return HttpResponse(placeholder)
