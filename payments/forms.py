# forms.py
from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['method']
        widgets = {
            'method': forms.RadioSelect  #show the method option with widget radio buttons
        }