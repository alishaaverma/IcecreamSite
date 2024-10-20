from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path("about",views.about, name='about'),
    path("services",views.services, name='services'),
    path("contactus",views.contactus, name='contactus'),
    path("feedback",views.feedback, name='feedback'),
    path("order",views.order, name='order'),
    path("drinks",views.drinks, name='drinks'),
    path("softy",views.softy, name='softy'),  
    path("shakes",views.shakes, name='shakes'), 
    path("icecream",views.icecream, name='icecream'),           
]