from django.conf.urls import url
from . import views           # This line is new!
#^ from the current directory, import views.py





urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    # Have the root url be handled by the views.py's index method (must specify index method in views.py)
    url(r'^test$', views.test)
]
