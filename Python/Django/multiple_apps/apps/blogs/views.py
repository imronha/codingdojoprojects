from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    placeholder = "Placeholder to display a blog index"
    return HttpResponse(placeholder)

    # if request.method == "POST":
    #     print "*"*50
    #     print request.POST
    #     print request.POST['name']
    #     print request.POST['desc']
    #     request.session['name'] = "test"  # more on session below
    #     print "*"*50
    #     return redirect("/")
    # else:
    #     return redirect("/")

def new(request):
    placeholder = "Placeholder to display a new form to create a new blog"
    return HttpResponse(placeholder)

def create(request):
    placeholder = "Placeholder for the /create"
    return HttpResponse(placeholder)

def show(request, number):
    placeholder = "Placeholder for the /show"+' '+number
    # print placeholder
    # print number
    return HttpResponse(placeholder)
