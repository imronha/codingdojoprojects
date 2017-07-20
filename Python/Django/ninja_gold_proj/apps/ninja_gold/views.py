from django.shortcuts import render, HttpResponse, redirect
import random
# Create your views here.

def index(request):
    if 'current_gold' not in request.session:
        request.session['current_gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, 'ninja_gold/index.html')

def process_money(request):
    if request.POST["building"] == 'farm':
        earned = random.randrange(10,21)
        request.session['current_gold'] += earned
        request.session['activities'].append("You earned "+str(earned)+" gold from the farm!")
    elif request.POST["building"] == 'cave':
        earned = random.randrange(5,11)
        request.session['current_gold'] += earned
        request.session['activities'].append("You earned "+str(earned)+" gold from the cave!")
    elif request.POST["building"] == 'house':
        earned = random.randrange(2,6)
        request.session['current_gold'] += earned
        request.session['activities'].append("You earned "+str(earned)+" gold from the house!")
    elif request.POST["building"] == 'casino':
        win = random.randrange(1,11)
        if win>0 and win<6:
            earned = random.randrange(0,51)
            request.session["current_gold"] += earned
            request.session["activities"].append("You earned "+str(earned)+" gold from the casino!")
        else:
            lost = random.randrange(0,51)
            request.session["current_gold"] -= lost
            request.session["activities"].append("You lost "+str(lost)+" gold from the casino...")

    print request.session['activities']
    return redirect('/ninja_gold')

def reset(request):
    request.session['current_gold'] = 0
    request.session['activities'] = []
    return redirect('/ninja_gold')
