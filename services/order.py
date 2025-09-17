"""Modulo que maneja toda la logica de las ordenes."""
from __future__ import annotations

from models.product import Product
from services.pricing import price_with_rules


class Order:
    """Clase que administra las ordenes."""

    def __init__(self, customer, rules):
        """Metodo init que inicia las ordenes con sus valores por default."""
        self.customer = customer
        self.rules = rules
        self.items = {}

    def add(self, product: Product, qty: int = 1) -> None:
        """Agrega un producto a la orden."""
        if qty <= 0:
            raise ValueError('qty must be > 0')
        if product.sku in self.items:
            prod, existing = self.items[product.sku]
            self.items[product.sku] = (prod, existing + qty)
        else:
            self.items[product.sku] = (product, qty)

    def subtotal(self) -> float:
        """Retorna el subtotal."""
        return round(
            sum(p.price * q for p, q in self.items.values()),
            2,
        )

    def total(self) -> float:
        """Retorna el total."""
        return price_with_rules(self.subtotal(), self.customer, self.rules)
