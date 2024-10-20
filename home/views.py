from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Order
from home.models import Feedback
from home.models import ContactUs
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
   # return HttpResponse("this is homepage")

def about(request):
    return render(request,'about.html')
   # return HttpResponse("this is about page")

def services(request):
    return render(request,'services.html') 
    #return HttpResponse("this is services page")
    
def drinks(request):
    return render(request,'drinks.html') 
    #return HttpResponse("this is drinks page")
    
def shakes(request):
    return render(request,'shakes.html') 
    #return HttpResponse("this is shakes page")
 
def icecream(request):
    return render(request,'icecream.html') 
    #return HttpResponse("this is icecream page")
    
def softy(request):
    return render(request,'softy.html') 
    #return HttpResponse("this is softy page")
    
def contactus(request):
    if request.method == "POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        address =request.POST.get('address')
        message =request.POST.get('message')
        message = ContactUs(name=name,email=email,address=address,message=message,date=datetime.today())
        message.save()
        messages.success(request, "your message has been sent!!")
    
    return render(request,'contactus.html') 
    #return HttpResponse("this is contactus page")
    
def feedback(request):
    if request.method == "POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        feedback =request.POST.get('feedback')
        feedback = Feedback(name=name,email=email,feedback=feedback,date=datetime.today())
        feedback.save()
        messages.success(request, "your feedback has been sent!!")
        
    return render(request,'feedback.html') 
    #return HttpResponse("this is feedback page")
    

def order(request):
    if request.method == "POST":
        first_name =request.POST.get('first_name')
        last_name =request.POST.get('last_name')
        email =request.POST.get('email')
        address =request.POST.get('address')
        state =request.POST.get('state')
        mobile_number =request.POST.get('mobile_number')
        message =request.POST.get('message')
        contact = Order(first_name=first_name,last_name=last_name,email=email,address=address,state=state,mobile_number=mobile_number,message=message,date=datetime.today())
        contact.save()
        messages.success(request, "your order has been sent!!")
        
    return render(request,'order.html')
    #return HttpResponse("this is order page")
