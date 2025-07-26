# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Payment
from .forms import PaymentForm
from orders.models import Order
from django.contrib.auth.decorators import login_required

@login_required
def process_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.order = order
            payment.user = request.user
            payment.amount = order.total_price
            payment.status = Payment.PaymentStatus.SUCCESS  # simulate a success payment
            payment.save()
            return redirect('payment_complete', pk=payment.pk)
    else:
        form = PaymentForm()

    return render(request, 'payments/process_payment.html', {
        'form': form,
        'order': order
    })

# @login_required
# def payment_complete(request, pk):
#     payment = get_object_or_404(Payment, pk=pk, user=request.user)
#     return render(request, 'payments/payment_complete.html', {
#         'payment': payment
#     })



# def payment_complete(request):
#     """displays payment success message and order details view"""
#     pass

# @login_required
# class PaymentListView(ListView):
#     model = Payment
#     template_name = 'payments/payments.html'
#     context_object_name = 'payments'
#     ordering = ['-created_at']