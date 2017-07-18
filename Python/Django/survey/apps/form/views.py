from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
def index(request):
    return render(request, 'form/index.html')

def process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comments'] = request.POST['comments']
    # print request.POST['name']
    # print request.POST['location']
    # print request.POST['language']
    # print request.POST['comments']
    return redirect('/result')

def result(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    info = {
        "name": request.session['name'],
        "location": request.session['location'],
        "language": request.session['language'],
        "comments": request.session['comments'],
        'count': request.session['count']
    }

    return render(request, "form/result.html", info)
