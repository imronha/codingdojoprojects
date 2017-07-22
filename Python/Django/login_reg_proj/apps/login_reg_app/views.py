from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your views here.
def index(request):
    return render(request, 'login_reg_app/index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        #print error message if fails validation
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        #Search the db to see if the user already exists
        found_user = User.objects.filter(email=request.POST['email'])
        if found_user.count() > 0:
            messages.error(request, "Email already taken.", extra_tags="email")
            return redirect('/')
        else:
            #If the found user doesnt exist, hash their pw and create user object
            hashed_pw = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt())
            new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed_pw)
            request.session['first_name'] = request.POST['first_name']
            request.session['last_name'] = request.POST['last_name']

    return redirect('/success')
        # return render(request, 'login_reg_app/index.html', )
def success(request):
    return render(request, 'login_reg_app/success.html')

def login(request):
    #Check to see if we find any users with the email provided
    found_users = User.objects.filter(email=request.POST['email'])
    if len(found_users) >0:
        #If found, check if their pw matches the hashed pw stored in db
        found_user= found_users.first()
        if bcrypt.checkpw(request.POST['pw'].encode(), found_user.password.encode()) == True:
            #Successfully logged in
            request.session['user_id'] = found_user.id
            request.session['user_name'] = found_user.first_name+' '+found_user.last_name
            print found_user
            return redirect('/success')
        else:
            messages.error(request, "Login failed", extra_tags="email")
            return redirect('/')
    else:
        messages.error(request, "Login failed", extra_tags="email")
        return redirect('/')
