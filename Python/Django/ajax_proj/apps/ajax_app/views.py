from django.shortcuts import render, HttpResponse
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, "ajax_app/index.html")

def posts(request):
	print request.POST

	return JsonResponse(request.POST)
