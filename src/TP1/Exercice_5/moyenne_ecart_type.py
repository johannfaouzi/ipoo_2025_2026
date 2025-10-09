from math import sqrt
from random import random


def compute_mean_and_std(n: int) -> tuple[float, float]:
    """Calcule la moyenne et l'écart-type d'échantillons aléatoires.

    Parameters
    ----------
    n : int
        Nombre d'échantillons à tirer

    Returns
    -------
    tuple
        Moyenne et écart-type

    Examples
    --------
    >>> mean, std = compute_mean_and_std(100_000)
    >>> mean
    0...
    >>> std
    0...
    >>> abs(mean - 0.5) < 1e-1
    True
    >>> abs(std - sqrt(1/12)) < 1e-1
    True
    """

    # Génère la liste de nombres aléatoires
    liste: list[float] = [random() for _ in range(n)]

    # Calcule la moyenne empirique
    mu: float = sum(liste) / n

    # Calcule l'écart-type empirique
    sigma: float = sqrt(sum(x**2 for x in liste) / n - mu**2)

    return mu, sigma
