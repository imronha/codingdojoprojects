from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    random_str = {
        "string": get_random_string(length=14)
    }
    print random_str
    print request.session['count']

    # placeholder = "Random word generator placeholder"
    return render(request, 'random_word_gen/index.html', random_str)
