

# Register your models here.
from django.contrib import admin
from.models import Menu, Order

class MenuAdmin(admin.ModelAdmin):
    list_display = ['id','name','price']
    search_fields = ['name']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','customer','menu_item','quantity','total_amount','order_status','created_at']
    list_filter = ['order_status','created_at']
    search_fields = ['customer__username','menu_item__name']