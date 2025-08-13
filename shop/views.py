from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, ProductImage
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

#@login_required
def home(request):
    return render(request, "shop/home.html")

#@login_required
def product_list(request, category_pk=None):
    """The product_list."""
    if category_pk:
        category = get_object_or_404(Category, pk=category_pk)
        products = Product.objects.filter(category=category).filter(available=True)
    else:
        category = None
        products = Product.objects.filter(available=True) # we are filtering to get only available products.
    return render(request, "shop/product-list.html", {"products": products, "category": category})

#@login_required
def product_detail(request, pk):
    #product = Product.objects.get(pk=pk)
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

def category_summary(request, search_term=''):
    if request.method == 'POST':
        search_term = request.POST['txt_search']

    if search_term == '':
        categories = Category.objects.all()
    else:
        categories = Category.objects.filter(name__icontains=search_term)

    return render(request, 'shop/category_summary.html', {'categories': categories, 'search_term': search_term})