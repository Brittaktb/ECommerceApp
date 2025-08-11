from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, ProductImage
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

#@login_required
def home(request):
    return render(request, "shop/home.html")

#@login_required
def product_list(request):
    """The product_list."""
    products = Product.objects.filter(available=True) # we are filtering to get only available products.
    return render(request, "shop/product-list.html", {"products": products})

#@login_required
def product_detail(request, pk):
    #product = Product.objects.get(pk=pk)
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

# from .models import Product, CartItem, Cart  # adapt your model names
# from django.contrib.auth.decorators import login_required

# @login_required
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id, availability=True)
#     cart, _ = Cart.objects.get_or_create(user=request.user)
#     item, created = CartItem.objects.get_or_create(cart=cart, product=product)
#     if not created:
#         item.quantity +=1
#         item.save()
#     return redirect('shop:product_list')