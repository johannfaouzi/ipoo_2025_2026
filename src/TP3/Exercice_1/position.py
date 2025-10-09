from typing import Any


def position(elt: Any, liste: list[Any], depart: int = 0) -> int:
    """Cherche la première occurrence d'un élément dans une liste.

    Parameters
    ----------
    elt :
        Élément recherché dans la liste.
    liste : list
        Liste à parcourir.
    depart : int (default = 0)
        Indice de départ pour le parcours de la liste.

    Returns
    -------
    int
        Indice de la première occurrence, -1 sinon.

    Examples
    --------
    >>> position(4, [2, 4, 10])
    1
    >>> position(4, [2, 4, 10], 2)
    -1
    >>> position(5, [2, 4, 10])
    -1
    """
    for i in range(depart, len(liste)):
        if liste[i] == elt:
            return i
    return -1
