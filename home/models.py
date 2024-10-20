from django.db import models

# Create your models here.
class Order(models.Model):
    first_name =models.CharField(max_length=200)
    last_name =models.CharField(max_length=200)
    email =models.EmailField(max_length=200)
    address =models.CharField(max_length=300)
    state =models.CharField(max_length=200)
    mobile_number =models.CharField(max_length=12)
    message =models.TextField()
    date =models.DateField()
    
    def __str__(self):
        return self.email
    
class Feedback(models.Model):
    name =models.CharField(max_length=200)
    email =models.EmailField(max_length=200)
    feedback =models.TextField()
    date =models.DateField()
    
    def __str__(self):
        return self.name
    
class ContactUs(models.Model):
    name =models.CharField(max_length=200)
    email =models.EmailField(max_length=200)
    address =models.EmailField(max_length=500)
    message =models.TextField()
    date =models.DateField()
    
    def __str__(self):
        return self.email