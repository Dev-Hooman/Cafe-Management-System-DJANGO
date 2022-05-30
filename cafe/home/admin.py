from django.contrib import admin

# Register your models here.
from home.models import ContactUs, Product, Reviews

admin.site.register(ContactUs)
admin.site.register(Product)
admin.site.register(Reviews)