from django.urls import path
from home import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ContactUs"),
    path('tracker/', views.tracker, name="TrackingStatus"),
    path('cart/', views.cart, name="cart"),
    path('food/',views.foodView, name="food"),
    path('checkout/', views.checkout, name="Checkout"),
    path('users/', views.reviewForm, name="review")
]
