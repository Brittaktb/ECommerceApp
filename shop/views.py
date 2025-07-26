from django.shortcuts import render
from .models import Product, Category
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    return render(request, "shop/home.html")

@login_required
def product_list(request):
    """The product_list."""
    products = Product.objects.filter(available=True) # we are filtering to get only available products.
    return render(request, "shop/shop.html", {"products": products})

@login_required
def product_detail(request):                              # we are filtering to get only available categories.
    category = Category.objects.filter(availability=True)
    return render(request, "shop/product_detail.html")

@login_required
def shop(request):
    return render(request, "shop/shop.html")