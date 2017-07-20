from __future__ import unicode_literals

from django.db import models

# Create your models here.
# class CourseManager(models.Manager):
#     def basic_validator(self, postdata):
#         errors = []
#         if len(postdata['name'] < 10):
#             errors['name'] = "Course name must be at least 10 characters long"
#         if len(postdata['desc'] < 15):
#             errors['desc'] = "Description must be at least 15 characters long"
#         return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
