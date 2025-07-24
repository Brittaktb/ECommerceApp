from django.shortcuts import render
from .models import Category, Product, ProductImage
# Create your views here.
def home(request):
    return render(request, "shop/home.html")

def product_list(request):
    """The product_list."""
    products = Product.objects.filter(availability=True) # we are filtering to get only available products.
    return render(request, "shop/shop.html", {"shop": products})

def product_detail(request):                              # we are filtering to get only available categories.
    category = Category.objects.filter(availability=True)