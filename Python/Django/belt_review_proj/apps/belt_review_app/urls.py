from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.register),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^books/add$', views.add_book_page),
    url(r'^books/add/success$', views.add_book_success),
    url(r'^books/(?P<id>\d+)$', views.book_info),
    url(r'^user/(?P<id>\d+)$', views.user_info),
    url(r'^add_review/(?P<id>\d+)$', views.add_review),
    url(r'^delete_review/(?P<id>\d+)$', views.delete_review),
    # url(r'^courses/destroy/(?P<course_id>\d+)$', views.delete_conf),
    # url(r'^courses/destroy_for_real/(?P<course_id>\d+)$', views.delete),
    # url(r'^users/(?P<user_id>\d+)$', views.show_users_and_update),
    # url(r'^users/(?P<user_id>\d+)/edit$', views.edit_users),
    # url(r'^users/(?P<user_id>\d+)/destroy$', views.delete_users),
]
