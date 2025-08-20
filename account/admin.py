from django.shortcuts import render 
from django.http import HttpResponse
from.models import menuitem
from django.db import DatabaseError
def menu_items_view(request):
    try:
        items = menuitem.objects.all()
        return render (request, "menu.html",{"items":items})
        except Databaseerror:
            return HttpResponse("sorry, we're experiencing database issues. please try again later.", status=500)
            except Exception as e:
                return HttpResponse(f"An unexpected error occurred: {str(e)}", status=500)