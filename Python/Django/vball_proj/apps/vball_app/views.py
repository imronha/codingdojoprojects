from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "vball_app/index.html")
