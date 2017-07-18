from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    placeholder = "Placeholder to display surveys created"
    return HttpResponse(placeholder)

def new(request):
    placeholder = "Placeholder for users to add a new survey"
    return HttpResponse(placeholder)
