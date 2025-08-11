from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

#@login_required


from django.shortcuts import render, get_object_or_404

def home(request):
    return render(request, "shop/home.html")

def product_list(request):
    products = Product.objects.filter(available=True)
    category_query = request.GET.get('category', '')
    if category_query:
        products = products.filter(category__name__icontains=category_query)
    return render(request, "shop/product-list.html", {"products": products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

# def home(request):
#     return render(request, "shop/home.html")

# #@login_required
# def product_list(request):
#     """The product_list."""
#     products = Product.objects.filter(available=True) # we are filtering to get only available products.
#     category_query = request.GET.get('category', '')
#     if category_query:
#         products = Product.objects.filter(category_id__name__icontains=category_query, available=True)
#     else:
#         products = Product.objects.filter(available=True)
#     return render(request, "shop/product-list.html", {"products": products})

# #@login_required
# def product_detail(request, pk):
#     #product = Product.objects.get(pk=pk)
#     product = get_object_or_404(Product, pk=pk)
#     return render(request, 'shop/product_detail.html', {'product': product})
 
    
#     # we are filtering to get only available categories.
#     category = Category.objects.filter(availability=True)
#     return render(request, "shop/product_detail.html")






# # from .models import Product, CartItem, Cart  # adapt your model names
# # from django.contrib.auth.decorators import login_required

# # @login_required
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id, availability=True)
#     cart, _ = Cart.objects.get_or_create(user=request.user)
#     item, created = CartItem.objects.get_or_create(cart=cart, product=product)
#     if not created:
#         item.quantity +=1
#         item.save()
#     return redirect('shop:product_list')