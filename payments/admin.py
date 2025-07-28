from django.contrib import admin
from .models import Payment
# Register your models here.


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """ list display shows selected product details """
    list_display = ['order_id', 'user_id', 'amount', 'method', 'status', 'created_at', 'updated_at']