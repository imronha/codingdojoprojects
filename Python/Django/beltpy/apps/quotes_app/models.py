from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = "Name must be at least 2 characters long."
        if len(postData['alias']) < 2:
            errors['alias'] = "Alias must be at least 2 characters long."
        if not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = "Email must be valid."
        if len(postData['pw']) < 8:
            errors['pw'] = "Password must be at least 8 characters long."
        if postData['pw'] != postData['pwconfirm']:
            errors['pw'] = "Password and confirmation must match."
        return errors

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()

class QuoteManager(models.Manager):
    def quote_validator(self, postData):
        errors = {}
        if len(postData['author']) ==0:
            errors['author'] = "Please include an author."
        if len(postData['quote']) == 0:
            errors['quote'] = "Please include a quote."
        return errors

class Quote(models.Model):
    content = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    quote_by = models.ManyToManyField(User, related_name="fav_quote")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = QuoteManager()

class Favorite(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User)
    quote = models.ForeignKey(Quote)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
