"""Modulo que se encarga de las notificaciones por correo, wa, etc."""


def send_email(to: str, subject: str, body: str) -> None:
    """Envia el mail a la persona confirmando la orden, PRUEBAS."""
    print(f'[EMAIL] To={to} | Subject={subject}\n{body}')
