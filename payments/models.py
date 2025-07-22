from django.db import models

# Create your models here.

class Payment(models.Model):
        class PaymentMethod(models.TextChoices):
            CARD = 'card', 'Credit/Debit Card'
            PAYPAL = 'paypal', 'PayPal'
            MANUAL = 'manual', 'Manual Transfer'

        class PaymentStatus(models.TextChoices):
            PENDING = 'pending', 'Pending'
            SUCCESS = 'success', 'Success'
            FAILED = 'failed', 'Failed'

        order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        amount = models.DecimalField(max_digits=10, decimal_places=2)
        method = models.CharField(max_length=20, choices=PaymentMethod.choices, default=PaymentMethod.CARD)
        status = models.CharField(max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return f'Payment #{self.id} - {self.status} - {self.amount}'