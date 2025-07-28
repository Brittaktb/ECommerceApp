from django.views.generic import ListView
from .models import Order, Product
from users.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect




# def order_create(request, product_id):
#     # Retrieve a product
#     product = get_object_or_404(Product, id=product_id)
#     customer_details = get_object_or_404(CustomUser, id=customuser_id)
#     if request.method == "POST":
#         #Get the product values
#             order = Order.objects.create(
#             first_name=request.user,
#             email=
#             phone_number=
#             address=
#             postal_code
#             city
#             created
#             updated
#             paid
#             total_items
#             total_price
#             discount
#             customer_id
#             )
#             return redirect("payments:pay", order.id)
#     form = OrderForm()
#     return render(request, "orders/orders.html", {"order": order,"form": form})
  

class OrderListView(ListView):
    model = Order
    template_name = 'orders/orders.html'
    context_object_name = 'orders'
    ordering = ['-created']


@login_required
def customer_orders_view(request):
    orders = Order.objects.filter(customer=request.user).order_by('-created')
    return render(request, 'orders/customer_orders.html', {'orders': orders})

