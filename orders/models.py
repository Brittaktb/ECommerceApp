from django.db import models
from users.models import CustomUser
from shop.models import Product
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(CustomUser, related_name="orders", null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    total_items = models.IntegerField(null=True)
    total_price = models.CharField(max_length=10, null=True)
    discount = models.IntegerField(default=0,
                                validators=[MinValueValidator(0),
                                            MaxValueValidator(100)])

    def __str__(self):
        return f"Order {self.id}"
    
    class Meta:
        ordering = ("-created",)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)