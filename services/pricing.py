"""Modulo que define las reglas de precios y sus funciones."""


from util.validators import ensure_percentage


class PricingRules:
    """Clase que define todas las reglas y logica de los precios."""

    def __init__(self, tax_rate=0.16, promo_discount=0.0):
        self.tax_rate = ensure_percentage(tax_rate, name='tax_rate')
        self.promo_discount = ensure_percentage(
            promo_discount, name='promo_discount'
        )


def price_with_rules(amount, customer, rules):
    """Retorna el precio con las reglas para un cliente individual asignado."""
    discount_factor = (1.0 - rules.promo_discount) * (
        1.0 - customer.tier_discount
    )
    base = amount * discount_factor
    total = base * (1.0 + rules.tax_rate)
    return round(total, 2)
