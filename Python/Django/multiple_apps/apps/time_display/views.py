from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from datetime import datetime

def index(request):
    date = datetime.now().date().strftime('%B %-d, %Y')
    time = datetime.now().time().strftime('%-I:%M %p')
    context = {
        'datetime' : [
            {'date': date},
            {'time': time},
        ]
    }
    # context = {
    #     "time": (strftime("%Y-%m-%d %H:%M %p", gmtime()))
    # }
    # print strftime("%Y-%m-%d %H:%M %p", gmtime())
    return render(request,'time_display/index.html', context)
