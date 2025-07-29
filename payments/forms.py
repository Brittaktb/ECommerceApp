# forms.py
from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    
    # card number only in forms, cause of PCI DSS
    # (Payment Card Industry Data Security Standard)
    card_number = forms.CharField(
    required=False,
    max_length=16,
    widget=forms.TextInput(attrs={'placeholder': 'Enter card number'}),
    label='Card Number'
    )
    class Meta:
        model = Payment
        fields = ['method']
        widgets = {
            'method': forms.RadioSelect  #show the method option with widget radio buttons
        }
    
    def clean_card_number(self):
        method = self.cleaned_data.get('method')
        card_number = self.cleaned_data.get('card_number')

        if method == Payment.PaymentMethod.CARD:
            if not card_number:
                raise forms.ValidationError("Card number is required for card payments.")
            if not card_number.isdigit() or len(card_number) != 16:
                raise forms.ValidationError("Card number must be 16 digits.")
            if card_number not in ['4242424242424242', '4111111111111111']:
                raise forms.ValidationError("Test card number not recognized.")

        return card_number