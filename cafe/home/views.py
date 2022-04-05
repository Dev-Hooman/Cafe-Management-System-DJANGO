from django.shortcuts import render, HttpResponse

from datetime import datetime as dt
from home.models import ContactUs

#for messages
from django.contrib import messages

def Home(request):
    context = {
        "variable1" : "Abdul Rehman",
        "variable2" : "xD Online 1 min ago"
    }
    return render(request, "index.html", context)
    #return HttpResponse("Welcome to cafe")

def about(request):
    return render(request, "aboutus.html")

def contactus(request):
    if request.method == "POST":
        help_name = request.POST.get('help_name')
        help_email = request.POST.get('help_email')
        help_desc = request.POST.get('help_desc')
        contact = ContactUs(name = help_name, email = help_email, desc = help_desc, date = dt.today())
        contact.save()
        messages.success(request, 'Your message has been sent, Successfully!')
    
    return render(request, "contactus.html")