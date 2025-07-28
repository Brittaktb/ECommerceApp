from django.shortcuts import render, get_object_or_404
from shop.models import Product


# Create your views here.
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "cart/add-to-cart.html", {"product": product})

def view_cart(request):
    return render(request, "cart/cart.html")