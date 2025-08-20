from django import forms
from .models import Order


class OrderForm(forms.ModelForm):

    #address = forms.CharField(max_length=255)
    #city = forms.CharField(max_length=100)
    #postal_code = forms.CharField(max_length=20)

    class Meta:
        model = Order
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'address',
            'postal_code',
            'city',
        ]