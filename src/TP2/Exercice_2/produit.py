def produit(liste: list[int]) -> int:
    """Effectue le produit des entiers d'une liste.

    Parameters
    ----------
    liste : list[int]
        Liste d'entiers.

    Returns
    -------
    int
        Produit des entiers de la liste.

    Examples
    --------
    >>> produit([1, 2, 3])
    6
    """
    if not isinstance(liste, list):
        raise TypeError("liste doit être une liste")
    res: int = 1
    for x in liste:
        if not isinstance(x, int):
            raise TypeError(
                f"Tous les éléments de la liste doivent être des entiers " f"({repr(x)} n'est pas un entier)"
            )
        res *= x
    return res
