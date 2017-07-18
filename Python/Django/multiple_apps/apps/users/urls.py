from django.conf.urls import url
from . import views
#^ from the current directory, import views.py





urlpatterns = [
    url(r'^', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^new$', views.register),
]
