def moyenne_mobile(entree: list[int | float], fenetre: int) -> list[float]:
    """Calcule la série des moyennes mobile

    Parameters
    ----------
    entree : list[int | float]
        Vecteur auquel appliquer la moyenne mobile.

    fenetre : int
        Taille de la fenêtre de la moyenne mobile.

    Returns
    -------
    list[float]

    Examples
    --------
    >>> moyenne_mobile([2, 3, 5, 7, 11, 13, 17], 4)
    [4.25, 6.5, 9.0, 12.0]
    """
    res: list[float] = [sum(entree[i : i + fenetre]) / fenetre for i in range(len(entree) - fenetre + 1)]
    return res
