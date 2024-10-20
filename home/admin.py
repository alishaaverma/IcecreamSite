from django.contrib import admin
from home.models import Order
from.models import Feedback
from.models import ContactUs

# Register your models here.
admin.site.register(Order)
admin.site.register(Feedback)
admin.site.register(ContactUs)
