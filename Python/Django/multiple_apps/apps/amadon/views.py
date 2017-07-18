from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'amadon/index.html')

def process(request):
    return redirect('/')
