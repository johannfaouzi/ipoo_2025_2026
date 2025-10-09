from typing import Any, Callable


def p(x: int) -> bool:
    """Test si un nombre est impair.

    Parameters
    ----------
    x : int
        Le nombre à tester.

    Returns
    -------
    bool
        True si x est impair, False sinon

    Examples
    --------
    >>> p(1)
    True
    >>> p(8)
    False
    """
    return x % 2 == 1


def filtrer(fonction: Callable[[Any], bool], liste: list[Any]) -> list[Any]:
    """Filtre une liste en appliquant une fonction à ses éléments.

    Parameters
    ----------
    fonction : function
        la fonction à appliquer
    liste : list
        la liste à transformer

    Returns
    -------
    list
        la liste filtrées des éléments renvoyant False

    Examples
    --------
    >>> filtrer(p, [1, 2, 3, 4, 5])
    [1, 3, 5]

    >>> filtrer(lambda x: x % 2 == 1, [1, 2, 3, 4, 5])
    [1, 3, 5]
    """
    return [e for e in liste if fonction(e)]
