

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import response

def menu_list(request):
    menu = [{"name": "Margherita Pizza", "description": "Classic pizza with cheese ","price":8.99},{"name":"Veggie Burger", "description":"Burger with grilled vegetables","price":6.49},{"name":"Pasta Alfredo","description":"Creamy Alfredo sauce pasta","price":7.99},]
    return Response(menu)

# Create your urls.py here.
 
from django.urls import path
from.views import menu_list

urlpatterns = [path('menu/', menu_list, name='menu-list'),]