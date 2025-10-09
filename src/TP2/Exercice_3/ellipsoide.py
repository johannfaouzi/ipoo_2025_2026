import pytest


def ellipsoide(
    point: tuple[int | float, int | float, int | float], axes: tuple[int | float, int | float, int | float]
) -> bool:
    """Détermine si un point fait partie de l'ellipsoïde.

    L'équation de l'ellipsoïde est :
        (x / a) ** 2 + (y / b) ** 2 (z / c) ** 2 == 1
    pour un point de coordonnées cartésiennes (x, y, z) et où a, b, c sont les demi-axes de l'ellipsoïde.

    Parameters
    ----------
    point : tuple[int or float]
        Coordonnées cartésiennes du point.

    axes : tuple[int or float]
        Demi-axes de l'ellipsoïde.

    Returns
    -------
    bool
        True si le point fait partie de l'ellipsoïde, False sinon.

    Examples
    --------
    >>> ellipsoide((1, 0, 0), (1, 1, 1))
    True
    >>> ellipsoide((2, 0, 0), (1, 1, 1))
    False
    >>> ellipsoide((2, 3, 4), (2, 3, 4))
    False
    """
    if not (isinstance(point, tuple) and (len(point) == 3)):
        raise ValueError("'point' doit être une instance de tuple de longeur 3.")

    if not (isinstance(axes, tuple) and (len(axes) == 3)):
        raise ValueError("'axes' doit être une instance de tuple de longeur 3.")

    if not all(isinstance(element, (int, float)) for element in point):
        raise ValueError("Tous les éléments de 'point' doivent être des instances de int ou float.")

    if not all(isinstance(element, (int, float)) and (element > 0) for element in axes):
        raise ValueError("Tous les éléments de 'axes' doivent être des instances de int ou float strictement positifs.")

    x, y, z = point
    a, b, c = axes
    return (x / a) ** 2 + (y / b) ** 2 + (z / c) ** 2 == pytest.approx(1)
