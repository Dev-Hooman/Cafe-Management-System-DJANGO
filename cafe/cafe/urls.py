from django.contrib import admin
from django.urls import path, include

#-----------------------------------------
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "SZABIST CAFE ADMIN"
admin.site.site_title = "SZABIST CAFE ADMIN Portal"
admin.site.index_title = "Welcome to Szabist Cafe Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("users.urls")),
    path('blog/', include("blog.urls")),
    path('', include("home.urls")),  #this is home

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)