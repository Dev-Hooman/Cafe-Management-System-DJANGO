from django.shortcuts import render, HttpResponse

from math import ceil

from datetime import datetime as dt
#models
from home.models import ContactUs
from home.models import Product
from home.models import Reviews

#for messages
from django.contrib import messages

from .forms import foodCategory

def Home(request):

    return render(request, "home/index.html")
    #return HttpResponse("Welcome to cafe")

def about(request):
    return render(request, "home/aboutus.html")

def contact(request):
    if request.method == "POST":
        help_name = request.POST.get('help_name')
        help_email = request.POST.get('help_email')
        help_desc = request.POST.get('help_desc')
        contact = ContactUs(name = help_name, email = help_email, desc = help_desc, date = dt.today())
        contact.save()
        messages.success(request, 'Your message has been sent, Successfully!')
    
    return render(request, "home/contactus.html")

def tracker(request):
    return render(request, 'home/tracker.html')

def cart(request):
    return render(request, 'home/cart.html')

def foodView(request):
    variable1 = request.POST.get('my_cat', 'default')

    
    allProducts = Product.objects.all()
    #n = len(allProducts)
    #slides_N = n//4 + ceil((n/4) + (n//4))
    allProds = []
    catprods = Product.objects.values('category')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        if cat == variable1:
            prod = Product.objects.filter(category=cat)
            n = len(prod)
            nSlides = n // 4 + ceil((n / 4) - (n // 4))
            allProds.append([prod, range(1, nSlides), nSlides])

    context = {
        'allProds':allProds,
        'food':allProducts,
    }
    

    return render(request, 'home/food.html', context)

def checkout(request):
    return render(request, 'home/checkout.html')

def reviewForm(request):
    '''
        This model is left for testing 
    
    '''
    r_var = request.POST.get('user_review', "NULL")
    review_name = request.user.username
    Myreview = Reviews(reviewer_name= review_name, review = r_var, review_date=dt.today())
    Myreview.save()
    messages.success(request, 'Your Review has been submitted')

    return render(request, "users/user.html")