from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index), #Goes to main
    url(r'^posts$', views.posts), #Goes to posts method

    # url(r'^users$', views.register), #Create user
    # url(r'^login$', views.login), #Create user
    # url(r'^quotes$', views.home_page),
    # url(r'^quotes/add$', views.add_quote),

]
