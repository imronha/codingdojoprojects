from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
    if request.method == "POST":
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email = request.POST['email'])
        return redirect('/users')
    else:
        context = {
            "all_users": User.objects.all()
        }
        return render(request, 'semi_restful_app/index.html', context)

def new_user(request):
    return render(request, 'semi_restful_app/new_users.html')

def show_users_and_update(request, user_id):
    if request.method == "POST":
        current_user = User.objects.filter(id=user_id)
        current_user.update(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email = request.POST['email'])
        return redirect('/users')
    else:
        current_user = User.objects.get(id=user_id)
        context = {
            "user" : current_user
        }
        return render(request, 'semi_restful_app/show_users.html', context)

def edit_users(request, user_id):
    current_user = User.objects.get(id=user_id)
    context = {
        "user" : current_user
    }
    return render(request, 'semi_restful_app/edit_users.html', context)

def delete_users(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/users')
