from django.shortcuts import render
from .models import Category, Product, ProductImage
# Create your views here.
def home(request):
    return render(request, "shop/home.html")

# def product_list(request):
#     return render(request, "", {"":})