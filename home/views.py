

# Create your views here.
from django.shortcuts import render 
def about (request):
    context = {"restaurant_name": "Gourmet paradise","description":"At Gourmet paradise, we serve fresh, locally sourced dishes crafted with passion. Our mission is to bring flavors from around the world to your plate, in a warm and welcoming atmosphere.","image_url":"/static/image/restaurant.jpg"}
return render(request,'about.html', context)


<html>
<head>
   <title>about - {{restaurant_name}}</title>
</head>
<body style="font-family: Arial, sans-serif; margin:0; background:#f8f9fa;">
<nav style="background:#343a40; padding:10px;">
<a href="/" style="color:white;text-decoration:none;margin-right:15px;">Home</a>
<a href="/about/" style="color:white; text-decoration:nine;">About</a> </nav>

<main style="padding:40px; text-align:center;">
<h1 style="color:#2c3e50;">About {{restaurant_name}}</h1>
<p style="color:#555; max-width:700px;margin:20px auto; font-size:1.1rem; line-height:1.6;">{{description}} </p> 
   {% if image_url %}
<img src="{{image_url}}" alt="{{restaurant_name}}" style="max-width:100%; border-radius:10px; box-shadow:0 4px 10px rgba (0,0,0,0.1);">

          {% endif %}
        </main>
    </body>
    </html>

# urls.py
from django.urls import path
from.views import home, about 

urlpatterns = [path('',home, name='home'),path('about/',about, name='about'),]

