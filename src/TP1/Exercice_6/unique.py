from typing import Any


def unique(liste: list[Any]) -> list[Any]:
    """Élimine les doublons d'une liste triée.

    Comportement non documenté si la liste n'est pas triée.

    Parameters
    ----------
    liste : list
        Une liste de valeurs numériques triées.

    Returns
    -------
    list
        La même liste, sans les doublons.

    Examples
    --------
    >>> unique([1, 1, 2, 2, 3, 3, 3, 4, 7])
    [1, 2, 3, 4, 7]
    """
    # Une astuce est de transformer la liste en dictionnaire, dont les clés
    # sont les éléments de la liste et dont les valeurs sont None, ce qui :
    # - supprime les doublons (les clés d'un dictionnaire sont uniques)
    # - conserve l'ordre des éléments (les dictionnaires sont ordonnés depuis
    #   Python 3.7)
    return list(dict.fromkeys(liste))
