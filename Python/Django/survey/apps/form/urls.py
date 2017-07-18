from django.conf.urls import url
from . import views
#^ from the current directory, import views.py





urlpatterns = [
    url(r'^$', views.index),
    url(r'^survey/process$', views.process),
    url(r'^result$', views.result),
    # url(r'^(?P<number>\d+)$', views.show),
]
