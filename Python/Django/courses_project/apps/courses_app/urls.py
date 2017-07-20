from django.conf.urls import url, include
from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^courses$', views.index),
    url(r'^courses/destroy/(?P<course_id>\d+)$', views.delete_conf),
    url(r'^courses/destroy_for_real/(?P<course_id>\d+)$', views.delete),
    # url(r'^users/(?P<user_id>\d+)$', views.show_users_and_update),
    # url(r'^users/(?P<user_id>\d+)/edit$', views.edit_users),
    # url(r'^users/(?P<user_id>\d+)/destroy$', views.delete_users),
]
