from django.contrib import admin
from .models import Order
# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """ list display shows selected product details """
    list_display = ['id', 'email', 'created', 'total_price', 'paid']
   
