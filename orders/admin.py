from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """ list display shows selected order details """
    list_display = ['id', 'email', 'created', 'total_price', 'paid']
   
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """ list display shows selected order_item details """
    list_display = ['id',
                    'product',
                    'price',
                    'quantity'
                ]