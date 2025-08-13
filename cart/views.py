from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Product
from cart.cart import Cart
from django.http import JsonResponse


# Create your views here.

def view_cart(request):
    cart = Cart(request)
    cart_products = cart.get_products()
    total_price = cart.get_total_price()
    return render(request, "cart/cart.html", {"cart_products": cart_products, "total_price": total_price})

def add_to_cart(request):
    # initialise the cart object (it will load whatever existing cart already exists, if one does)
    cart = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        # lookup product in database
        product = get_object_or_404(Product, id=product_id)

        # save to session
        cart.add(product=product, quantity=product_qty)

        # get cart quantity
        cart_quantity = cart.__len__()

        # Return response
        # return JsonResponse({'product_id': product_id})
        return JsonResponse({'qty': cart_quantity})
    else:
        return JsonResponse({'status': False})

    # return render(request, "cart/add-to-cart.html", {"product": product})

def delete_from_cart(request):
    # initialise the cart object
    cart = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id'))

        # lookup product in database
        product = get_object_or_404(Product, id=product_id)

        # save to session
        cart.remove(product=product)

        # get cart quantity
        cart_quantity = cart.__len__()

        # Return response
        # return JsonResponse({'product_id': product_id})
        return JsonResponse({'qty': cart_quantity})
    else:
        return JsonResponse({'status': False})

def update_cart(request):
    # initialise the cart object
    cart = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        # lookup product in database
        product = get_object_or_404(Product, id=product_id)

        # save to session
        cart.add(product=product, quantity=product_qty, override_quantity=True)

        # get cart quantity
        cart_quantity = cart.__len__()

        # Return response
        # return JsonResponse({'product_id': product_id})
        return JsonResponse({'qty': cart_quantity})
    else:
        return JsonResponse({'status': False})