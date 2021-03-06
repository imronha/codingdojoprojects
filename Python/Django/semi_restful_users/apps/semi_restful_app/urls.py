from django.conf.urls import url, include
from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^users$', views.index),
    url(r'^users/new$', views.new_user),
    url(r'^users/(?P<user_id>\d+)$', views.show_users_and_update),
    url(r'^users/(?P<user_id>\d+)/edit$', views.edit_users),
    url(r'^users/(?P<user_id>\d+)/destroy$', views.delete_users),
]
