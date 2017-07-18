from django.conf.urls import url
from . import views
#^ from the current directory, import views.py





urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<number>\d+)$', views.show),
]
