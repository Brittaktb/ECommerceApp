from django.shortcuts import render, get_object_or_404
from shop.models import Product
from .cart import Cart
from django.http import JsonResponse


# Create your views here.

def cart(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    totals = cart.cart_total()

    # product + amount  as subtotal as list
    items = []
    for product in cart_products:
        qty = quantities.get(str(product.id), {}).get('quantity', 0)
        subtotal = product.price * qty
        items.append({'product': product, 'quantity': qty, 'subtotal': subtotal})

    return render(request, "cart/cart.html", {
        "items": items,
        "totals": totals
    })

def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)

        cart_quantity = len(cart)  # Anzahl aller Artikel im Warenkorb
        return JsonResponse({'qty': cart_quantity})
  

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get Stuff
        product_id = int(request.POST.get('product_id'))
        #call delete Function in Cart
        cart.delete(product=product_id)
        
        response = JsonResponse({'product': product_id})
        #return redirect('cart')
        return response


    
def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get Stuff
        product_id = request.POST.get('product_id')
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product=product_id, quantity = product_qty)

        response = JsonResponse({'qty': product_qty})
        #return redirect('cart')
        return response
