

# Create your models here.
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length-100)
    def__str__(self):
        return self.name

#views.py
from django.shortcuts import render
from.models import Restaurant
def home(request):
    restaurant = Restaurant.objects.first()
    return render(request,'home.html',{'restaurant_name':restaurant.name if restaurant else 'Our Restaurant'})