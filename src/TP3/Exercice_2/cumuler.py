from typing import Any, Callable


def g(x: int | float, y: int | float) -> int | float:
    """Produit de deux nombres

    Parameters
    ----------
    x : int or float
        le premier nombre à multiplier
    y : int or float
        le deuxième nombre à multiplier

    Returns
    -------
    float
        le produit

    Examples
    --------
    >>> g(2, 4)
    8
    """
    return x * y


def cumuler(fonction: Callable[[Any, Any], Any], liste: list[Any]) -> Any:
    """Cumule les éléments d'une liste.

    Réduit la longueur de la liste en appliquant itérativement une fonction.

    Parameters
    ----------
    fonction : function
        la fonction à appliquer
    liste : list
        la liste à cumuler

    Returns
    -------
    ?
        le résultat de la fonction

    Examples
    --------
    >>> cumuler(g, [1, 2, 3, 4, 5])
    120

    >>> cumuler(lambda x, y: x * y, [1, 2, 3, 4, 5])
    120
    """
    # Renvoie un erreur si la liste est trop courte
    assert len(liste) > 1

    resultat = fonction(*liste[:2])
    for e in liste[2:]:
        resultat = fonction(resultat, e)
    return resultat
