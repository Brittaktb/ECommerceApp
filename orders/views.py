from django.views.generic import ListView
from .models import Order, Product, OrderItem
from users.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import OrderForm
from cart.cart import Cart

@login_required
def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    total_price = cart.cart_total()
    total_items = cart.__len__()

    if not cart_products:
        return redirect('cart:cart')

    # Total amount Cart items
    #total_items = sum(quantities[str(p.id)]['quantity'] for p in cart_products)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.total_items = total_items
            order.total_price = f"{total_price:.2f}"
            order.save()

            # set up OrderItems from cart
            for product in cart_products:
                qty = quantities.get(str(product.id), {}).get('quantity', 0)
                price = product.price  
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    price=price,
                    quantity=qty
                )

            # delete Cart
            request.session['cart'] = {}
            request.session.modified = True

            return redirect('payments:process_payment', order_id= int(order.id))
    else:
        user = request.user
        initial_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'phone_number': user.phone_number if hasattr(user, 'phone_number') else '',
            'address': user.address if hasattr(user, 'address') else '',
            'postal_code': user.postal_code if hasattr(user, 'postal_code') else '',
            'city': user.city if hasattr(user, 'city') else '',
        }
        form = OrderForm(initial=initial_data)

    return render(request, 'orders/checkout.html', {
        'form': form,
        'items': [{
            'product': p,
            'quantity': quantities.get(str(p.id), {}).get('quantity', 0),
            'subtotal': p.price * quantities.get(str(p.id), {}).get('quantity', 0)
        } for p in cart_products],
        'total_price': total_price,
        'total_items': total_items,
    })

class OrderListView(ListView):
    model = Order
    template_name = 'orders/orders.html'
    context_object_name = 'orders'
    ordering = ['-created']


@login_required
def customer_orders_view(request):
    orders = Order.objects.filter(customer=request.user).order_by('-created')
    return render(request, 'orders/customer_orders.html', {'orders': orders})

