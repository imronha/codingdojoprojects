from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index), #Goes to main
    url(r'^posts$', views.posts), #Goes to posts method
    url(r'^list$', views.list, name='list')
]
#
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)    urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_URL)
