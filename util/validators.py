"""Utilidades de validación simples."""


def ensure_percentage(value: float, *, name: str) -> float:
    """Valida que `value` esté en [0.0, 1.0].

    Parameters
    ----------
    value : float
        Valor a validar.
    name : str
        Nombre lógico del campo para mensajes.

    Returns
    -------
    float
        El mismo valor si es válido.

    Raises
    ------
    ValueError
        Si el valor está fuera de rango.
    """
    if not 0.0 <= value <= 1.0:
        raise ValueError(f'{name} must be between 0.0 and 1.0')
    return value
