from typing import Any

from .position import position


def sous_liste(petite_liste: list[Any], grande_liste: list[Any]) -> bool:
    """Vérifie si tous les éléments d'une liste apparaissent dans une autre.

    Vérifie que les doublons sont présents, et que tous sont dans le même
    ordre.

    Parameters
    ----------
    petite_liste : list
        Liste des éléments à vérifier.
    grande_liste : list
        Liste à parcourir pour vérification.

    Returns
    -------
    bool
        petite_liste est-elle un sous-ensemble de grande_liste ?

    Examples
    --------
    >>> sous_liste([2, 4, 10], [1, 2, 4, 5, 8, 10, 12])
    True
    >>> sous_liste([2, 4, 4, 10], [1, 2, 4, 5, 4, 6, 8, 10, 12])
    True
    >>> sous_liste([2, 10, 4], [1, 2, 4, 5, 8, 10, 12])
    False
    """
    next_scan = 0
    for e in petite_liste:
        tmp = position(e, grande_liste, next_scan)
        if tmp == -1:
            return False
        next_scan = tmp + 1
    return True
