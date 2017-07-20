from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'amadon/index.html')

def process(request, product_num):
    if 'count' not in request.session:
        request.session['count'] = 0
    if 'total' not in request.session:
        request.session['total'] = 0
        request.session['current_charge']=0
    if product_num == '1':
        request.session['current_charge'] = 19.99
    elif product_num == '2':
        request.session['current_charge'] = 29.99
    elif product_num == '3':
        request.session['current_charge'] = 9.99
    elif product_num == '4':
        request.session['current_charge'] = 49.99

    quantity = int(request.POST['quantity'])
    request.session['current_charge'] *= quantity
    request.session['count'] += quantity
    request.session['total'] += request.session['current_charge']
    print request.session['current_charge']
    print request.session['count']
    print request.session['total']
    return redirect('/amadon/checkout')

def checkout(request):
    return render(request, 'amadon/checkout.html')

def reset(request):
    request.session['count'] = 0
    request.session['total'] = 0
    request.session['current_charge']=0
    return redirect('/amadon')
