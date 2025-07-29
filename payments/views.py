# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin  # necessary for PaymentListView working with classes
from .models import Payment
from .forms import PaymentForm
from orders.models import Order
from django.contrib.auth.decorators import login_required #nessessary for working with @login_required & functions 
from decimal import Decimal
from django.contrib import messages

class PaymentListView(LoginRequiredMixin, ListView):  #
    model = Payment
    template_name = 'payments/payments.html'
    context_object_name = 'payments'
    ordering = ['-created_at']
    login_url = '/accounts/login/'
    
    
@login_required
def customer_payments_view(request):
    payments = Payment.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'payments/customer_payments.html', {'payments': payments})

@login_required
def process_payment(request, order_id=6):
    order = get_object_or_404(Order, id=order_id)
    form = PaymentForm() # initiate the PaymentForm with payments methods

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        #validation of card number happens in forms
        if form.is_valid():
            payment = form.save(commit=False)
            payment.order = order
            payment.user = request.user
            price_str = order.total_price.replace("€", "").replace(",", ".").strip()
            payment.amount = Decimal(price_str)
            
            if form.cleaned_data['method'] == Payment.PaymentMethod.MANUAL:
                payment.status = Payment.PaymentStatus.PENDING  # simulates a pending payment
            else: 
                payment.status = Payment.PaymentStatus.SUCCESS  # simulates a success payment  
            
            payment.save()
            
            #cart.clean
            #product.available = False

            return redirect('payments:payment_complete', pk=payment.pk)
        
    return render(request, 'payments/process_payment.html', {
        'form': form,
        'order': order
    })

@login_required
def payment_complete(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if payment.status == Payment.PaymentStatus.SUCCESS:
        messages.success(request, "Payment done successfully.")
        messages.success(request, "Thank you for your purchase!")
    elif payment.status == Payment.PaymentStatus.PENDING:
        messages.success(request, "Payment pending.")
    return render(request, 'payments/payment_complete.html', {
        'payment': payment
    })




