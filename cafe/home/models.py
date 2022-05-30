from distutils.command.upload import upload
from unicodedata import category
from django.db import models
from users.models import userAccount


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.TextField()
    pub_date = models.DateField()
    image = models.ImageField(upload_to="cafeItems/images", default="")
    
    def __str__(self):
        return self.product_name
    

class Reviews(models.Model):
    reviewer_name = models.CharField(max_length=50)
    review = models.TextField()
    review_date = models.DateField()

    def __str__(self):
        return self.reviewer_name

