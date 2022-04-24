from django.contrib import admin
from django.urls import path, include

#-----------------------------------------

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url

admin.site.site_header = "CAFE DI DIVINE ADMIN"
admin.site.site_title = "CAFE DI DIVINE ADMIN Portal"
admin.site.index_title = "Welcome to CAFE DI DIVINE Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("users.urls")),
    path('', include("home.urls")),  #this is home


    url(r'^media/(?P<path>.*)$', serve,{'document_root':  settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROUTE)
