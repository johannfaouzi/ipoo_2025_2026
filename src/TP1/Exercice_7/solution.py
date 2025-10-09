from typing import Callable


def solution(f: Callable[[int | float], int | float], a: int | float, b: int | float, epsilon: float) -> float:
    """Trouve un zéro d'une fonction par dichotomie.

    Résout l'équation f(x_0) = 0 pour x dans [a, b]. La solution
    retournée x est telle que x appartient à [x_0 - epsilon, x_0 + epsilon].

    Parameters
    ----------
    f : function
        La fonction dont on cherche le zero.
    a : float
        La borne inférieure de l'intervalle de recherche.
    b : float
        La borne supérieure de l'intervalle de recherche.
    epsilon : float
        La distance maximale à une solution.

    Returns
    -------
    float
        Une solution approchée x de f(x) = 0

    Examples
    --------
    >>> from math import cos, pi
    >>> x = solution(cos, 1, 3, 1e-3)
    >>> x
    1.57...
    >>> abs(x - pi / 2) < 1e-3
    True

    >>> from math import sqrt
    >>> x = solution(lambda x : x - sqrt(2), 0, 2, 1e-6)
    >>> x
    1.41...
    >>> abs(x - sqrt(2)) < 1e-6
    True

    """
    c: float
    while (b - a) > 2 * epsilon:
        c = (a + b) / 2

        # Si a et c ont le même signe, le nouvel interval est [c, b],
        # sinon le nouvel interval est [a, c].
        if (f(a) < 0) is (f(c) < 0):
            a = c
        else:
            b = c

    return (a + b) / 2
