"""Modulo para hacer pruebas con los precios."""

from models.customer import Customer
from services.pricing import PricingRules, price_with_rules

TEST_PRICE = 88.56


def test_price():
    """Funcion base para probar precios."""
    c = Customer(id='u1', name='Ana', tier_discount=0.1)
    rules = PricingRules(tax_rate=0.16, promo_discount=0.05)
    assert price_with_rules(100.0, c, rules) == TEST_PRICE
