from django.shortcuts import render 
def menu_list(request):
    menu_items = [{"name": "Margherita pizza", "price": 8.99}, {"name": "pasta Alfredo","price:10.99"}, {"name":"chocolate lava cake","price":4.99},]
    return render(request,"menu_list.html",{"menu_items": menu_itemms})