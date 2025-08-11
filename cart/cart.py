from django.conf import settings
from shop.models import Product
from decimal import Decimal


from django.conf import settings
from shop.models import Product
from decimal import Decimal

class Cart():
    def __init__(self, request):
        self.session = request.session
        
        cart = self.session.get('cart')
        if 'cart' not in request.session:
            cart = self.session['cart'] = {}
        
        self.cart = cart

    def save(self):
        """Mark session as modified so Django saves it."""
        self.session['cart'] = self.cart
        self.session.modified = True
        
    def add(self, product, quantity, override_quantity=False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }

        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()
        
    def update(self, product, quantity):
        product_id = str(product)
        quantity = int(quantity)

        if product_id in self.cart:
            self.cart[product_id]['quantity'] = quantity
        else:
            product_obj = Product.objects.get(id=product_id)
            self.cart[product_id] = {
                'quantity': quantity,
                'price': str(product_obj.price)
            }

        self.session.modified = True


    def cart_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        
        total = Decimal('0')
        for key, value in self.cart.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    total += Decimal(value['price']) * value['quantity']
        return total

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_prods(self):
        product_ids = self.cart.keys()
        return Product.objects.filter(id__in=product_ids)

    def get_quants(self):
        return self.cart
        
    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()


