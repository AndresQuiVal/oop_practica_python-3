"""Clase para crear un customer y su logica de operacion."""


class Customer:
    """Clase para la logica del cliente y su interaccion con la app."""

    def __init__(self, id, name, tier_discount):
        """Inicializa la clase de customer."""
        self.MAXBOUND = 0.8
        self.MINBOUND = 0.0
        self.id = id
        self.name = name
        self.tier_discount = tier_discount
        if not self.MINBOUND <= self.tier_discount <= self.MAXBOUND:
            raise ValueError('tier_discount must be between 0.0 and 0.8')
