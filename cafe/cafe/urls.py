from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "CAFE DI DIVINE ADMIN"
admin.site.site_title = "CAFE DI DIVINE ADMIN Portal"
admin.site.index_title = "Welcome to CAFE DI DIVINE Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("users.urls")),
    path('', include("home.urls")),  #this is home
]
