"""Modulo para administar los productos en el ecommerce."""


class Product:
    """Clase para administrar productos en la app de ecommerce."""

    def __init__(self, sku, name, price):
        self.sku = sku
        self.name = name
        self.price = price
        if self.price < 0:
            raise ValueError('price must be non-negative')

    def __setattr__(self, name, value):
        """Sobreescribimos el dunder method para que tenga su handler."""
        if hasattr(self, name):
            raise AttributeError(f"can't set attribute '{name}'")
        super().__setattr__(name, value)
