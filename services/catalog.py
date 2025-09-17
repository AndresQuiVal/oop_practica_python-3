"""Modulo que almacena toda la logica de catalogos dentro de la app."""

from __future__ import annotations


class Catalog:
    """Catalogo de productos dentro de la app."""

    def __init__(self, items=None):
        """Inicializa los productos del catalogo."""
        self._items = items or {}

    @classmethod
    def from_iterable(cls, items):
        """Itera entre los productos del catalogo."""
        return cls({p.sku: p for p in items})

    def get(self, sku: str):
        """Obtiene un producto del catalogo con un sku."""
        return self._items.get(sku)

    def all(self):
        """Obtiene todos los productos del catalogo."""
        return self._items.values()
