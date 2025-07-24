class Cart(object):  # Request object
    def __init__(self, request):
        """
        Initialize the cart.
        """
        pass

    def add(self, product, quantity=1, override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        pass

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        pass

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        pass

    def __len__(self):
        """
        Count all items in the cart.
        """
        pass

    def get_total_price(self):
        pass

    def clear(self):
        """Removes cart from the session."""
        pass

    def get_discount(self):
        pass

    def get_total_price_after_discount(self):
        pass
