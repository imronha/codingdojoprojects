from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from datetime import datetime

# Create your views here.
def index(request):
    # request.session['context'] = []
    # print request.session['context']
    return render(request, 'session_words/index.html')

def process(request):
    if 'context' not in request.session:
        request.session['context'] = []
    now = strftime("%Y-%m-%d %H:%M")
    if 'size' in request.POST:
        size = request.POST['size']
    else:
        size = 12
    given_word = {
        "word": request.POST['word'],
        "color": request.POST['color'],
        "date": str(now),
        "size": size
    }
    # print request.POST['size']
    request.session['context'].append(given_word)
    request.session.modified = True
    # info = request.session['context']
    # print info
    return redirect('/session_words')

def delete(request):
    request.session['context'] = []
    print request.session['context']
    return redirect('/session_words')
