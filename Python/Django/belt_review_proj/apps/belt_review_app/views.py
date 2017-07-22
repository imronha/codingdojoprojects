from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Book, Review
import re
import bcrypt

# ----------------- Registration and user log in validation ---------------------#
def index(request):
    return render(request, 'belt_review_app/index.html')

def register(request):
    errors = User.objects.user_validator(request.POST)
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
            messages.success(request, 'Successfully registered, you may now log in.')
            return redirect('/')
        # return render(request, 'login_reg_app/index.html', )
def success(request):
    reviews = Review.objects.all().order_by('-created_at')[:3]
    books_with_reviews = []
    books_with_reviews_titles = []
    reviewed = Review.objects.all()
    for review in reviewed:
        if review.book.title not in books_with_reviews_titles:
            books_with_reviews_titles.append(review.book.title)
            books_with_reviews.append(review.book)
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        "reviews": reviews,
        "books": books_with_reviews
    }
    # context = {
    #     "all_books": Book.objects.all()
    # }
    return render(request, 'belt_review_app/books_wall.html', context)

def login(request):
    #Check to see if we find any users with the email provided
    found_users = User.objects.filter(email=request.POST['email'])
    if len(found_users) >0:
        #If found, check if their pw matches the hashed pw stored in db
        found_user= found_users.first()
        if bcrypt.checkpw(request.POST['pw'].encode(), found_user.password.encode()) == True:
            #Successfully logged in
            request.session['user_id'] = found_user.id
            request.session['first_name'] = found_user.first_name
            print found_user
            return redirect('/success')
        else:
            messages.error(request, "Login failed", extra_tags="email")
            return redirect('/')
    else:
        messages.error(request, "Login failed", extra_tags="email")
        return redirect('/')

def logout(request):
    del request.session['user_id']
    del request.session['user_name']
    return redirect('/')

#-------------------------- End Login/reg validation -----------------------------#
def add_book_page(request):
    return render(request, 'belt_review_app/add_book.html')

def add_book_success(request):
    #Check to make sure user fills out all fields for book
    errors = Book.objects.book_validator(request.POST)
    if len(errors):
        #print error message if fails validation
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/books/add')
    else:
        user = User.objects.get(id=request.session['user_id'])
        book = Book.objects.create(title = request.POST['title'], author=request.POST['author'])
        Review.objects.create(content=request.POST['review'], rating=request.POST['rating'], user=user, book=book)
        book.reviewed.add(user)
        return redirect('/books/'+str(book.id))

def add_review(request, id):
    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=id)
    Review.objects.create(content=request.POST['review'], rating=request.POST['rating'], user=user, book=book)
    book.reviewed.add(user)
    return redirect('/books/'+str(id))

def delete_review(request, id):
    Review.objects.get(id=id).delete()
    return redirect('/success')

def book_info(request, id):
    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=id)
    context = {
        "user": user,
        "book": book,
        "reviews": Review.objects.filter(book=book)
    }
    return render(request, "belt_review_app/book_page.html", context)

def user_info(request, id):
    user = User.objects.get(id=id)
    print User.objects.all().values()
    context = {
        "user": user,
        "books": user.reviewed.all(),
        "reviews": Review.objects.filter(user=user)
    }
    return render(request, "belt_review_app/user_page.html", context)
def add_book(request):
    return redirect('/success')
