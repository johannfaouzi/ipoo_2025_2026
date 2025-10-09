from typing import Any, Callable


def f(x: int | float) -> int | float:
    """Fonction renvoyant le carré d'un nombre.

    Parameters
    ----------
    x : float
        valeur à transformer

    Returns
    -------
    float
        carré de x

    Examples
    --------
    >>> f(2)
    4
    """
    return x**2


def transformer(fonction: Callable[[Any], Any], liste: list[Any]) -> list[Any]:
    """Applique une fonction à chaque élément d'une liste.

    Parameters
    ----------
    fonction : function
        la fonction à appliquer
    liste : list
        la liste à transformer

    Returns
    -------
    list
        la liste transformée

    Examples
    --------
    >>> transformer(f, [1, 2, 3, 4, 5])
    [1, 4, 9, 16, 25]

    >>> transformer(lambda x: x ** 2, [1, 2, 3, 4, 5])
    [1, 4, 9, 16, 25]
    """
    # Solution avec la fonction native map : list(map(fonction, liste))
    return [fonction(e) for e in liste]
