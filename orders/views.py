

# Create your views here.
from django.shortcuts import render
from. models import Restaurant
def about (request):
    restaurant = Restaurant.objects.first()
    return render(request,'about.html,'{'restaurant': restaurant})

#Html
<!DOCTYPE html>
<html>
<head>
  <title>About - {{restaurant.name}}</title>
  <style>
  body{font-family: Arial,sans-serif; margin:0; padding:0;}
  header {background: #333; padding: 10px;}
  nav s {color:white; margin-right: 15px; text-decoration: none;}.container {max-width:800px; margin: auto; padding:20px;}
  img{max-width:100%; height: auto; border-radius:10px;}
  </head>
  <body>
   <header>
   <nav>
   <a href="{% url 'home'%}"> Home</a>
   <a href="{%url 'about'%}">About</a>
   </nav>
   </header>
   <div class="container">
   <h1>About{{restaurant.name}}<h1> {% if restaurant.image %}
   <img src="{{restaurant.image.url}}" alt="{{restaurant.name}]">
   {% endif %}
   <p> {{restaurant.description}}</p>
   </div>
   </body>
   </html>


   #model.py
   from django.db import models
   class Restaurant(models.Model):
    name = models.CharField(max.Model=100)
    description = models.TextField(blank=True)
    image  = models.ImageField(upload_to='restaurant_images/', blank=True, null=True)
    def__str__(self):
             return self.name
