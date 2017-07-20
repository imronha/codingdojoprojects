from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process/(?P<product_num>\d+)$', views.process),
    url(r'^checkout$', views.checkout),
    url(r'^reset$', views.reset)


]
