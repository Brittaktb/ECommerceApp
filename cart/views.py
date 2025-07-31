from django.shortcuts import render, get_object_or_404
from shop.models import Product
from cart.cart import Cart


# Create your views here.
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # initialise the cart object (it will load whatever existing cart already exists, if one does)
    cart = Cart(request)
    # add product
    cart.add(product)

    return render(request, "cart/add-to-cart.html", {"product": product})

def view_cart(request):
    # TODO: test my todos
    return render(request, "cart/cart.html")