

# Create your models here.
from django.db import models
from django.contrib.auth.models import User 

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6,decimal_places=2)

    def__str__(self):
        return self.name
class Order(models.Model):
    STATUS_CHOICES = [('PENDING', 'Pending'),('CONFIRMED','Confirmed'),('DELIVERED','Delvired'),('CANCELLED','Cancelled'),]
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu,on_delete=models.CASCADE)
    quantity = models.PostiveIntegerField(default=1)
    total_amount = models.DecimalField(max_digits=8,decimal_places=2)
    order_status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
     def__str__(self):
        return f"Order #{self.id} by {self.customer.username}"