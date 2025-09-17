"""Modulo principal."""

from models.customer import Customer
from models.product import Product
from services.catalog import Catalog
from services.notifications import send_email
from services.order import Order
from services.pricing import PricingRules


def main():
    """Funcion base para ejecutar el programa de ecommerce fitness."""
    # Datos base
    catalog = Catalog.from_iterable(
        [
            Product('SKU-001', 'Proteína Whey 2lb', 599.0),
            Product('SKU-002', 'Creatina Monohidratada 300g', 349.0),
            Product('SKU-003', 'Shaker 700ml', 149.0),
        ]
    )
    customer = Customer('c-100', 'Diego', tier_discount=0.10)
    rules = PricingRules(tax_rate=0.16, promo_discount=0.05)

    # Orden
    order = Order(customer, rules)
    order.add(catalog.get('SKU-001'))
    order.add(catalog.get('SKU-003'), qty=2)

    # Resultados
    print('--- RESUMEN DEL PEDIDO ---')
    print(f'Subtotal: ${order.subtotal():.2f}')
    print(f'Total:    ${order.total():.2f}')

    # Notificación (simulada)
    send_email(
        to='andres.quiroz@iteso.mx',
        subject='Gracias por tu compra',
        body=f'Tu total es ${order.total():.2f}. ¡Vuelve pronto!',
    )


if __name__ == '__main__':
    main()
