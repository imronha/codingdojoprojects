from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters long."
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters long."
        if not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = "Email must be valid."
        if len(postData['pw']) < 8:
            errors['pw'] = "Password must be at least 8 characters long."
        if postData['pw'] != postData['pwconfirm']:
            errors['pw'] = "Password and confirmation must match."
        return errors

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['title']) ==0:
            errors['title'] = "Please include a book title."
        if len(postData['author']) == 0:
            errors['author'] = "Please include an author."
        if len(postData['review']) == 0:
            errors['review'] = "Please include a review."
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    reviewed = models.ManyToManyField(User, related_name="reviewed")
    # reviewed = models.ManyToManyField(User, related_name="reviewed")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BookManager()

class Review(models.Model):
    rating = models.IntegerField()
    content = models.TextField()
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
