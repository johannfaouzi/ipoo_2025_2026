from typing import Any


def list_new_mat(nl: int, nc: int) -> list[list[Any]]:
    """Crée une nouvelle matrice vide sous forme de liste de listes.

    Une matrice vide n'est constituée que de zéros.

    Parameters
    ----------
    nl : int
        nombre de lignes
    nc : int
        nombre de colonnes

    Returns
    -------
    list
        liste de listes de zéros représentant la matrice

    Examples
    --------
    >>> list_new_mat(2, 3)
    [[0, 0, 0], [0, 0, 0]]
    """
    # Solution possible : [[0 for _ in range(nc)] for _ in range(nl)]
    # Solution qui NE marche PAS : return [[0] * nc] * nl
    # La liste [0] * nc n'est pas copiée avec le code [[0] * nc] * nl,
    # ce qui fait que modifier une liste (c'est-à-dire une ligne) modifie
    # toutes les listes (c'est-à-dire toutes les lignes).

    # Solution la plus rapide : elle marche car ici les listes (lignes) sont
    # copiées, ce qui fait que modifier une liste (ligne) ne modifie pas les
    # autres.
    # [0] * nc marche car les entiers (int) sont immutables.
    return [[0] * nc for _ in range(nl)]


def list_set_mat(m: list[list[Any]], i: int, j: int, x: Any) -> None:
    """Change une entrée d'une matrice.

    Parameters
    ----------
    m : list
        La matrice à modifier.
    i : int
        L'indice de la ligne à modifier.
    j : int
        L'indice de la colonne à modifier.
    x
        La nouvelle valeur.

    Examples
    --------
    >>> m = list_new_mat(2, 3)
    >>> list_set_mat(m, 0, 0, 3)
    >>> m
    [[3, 0, 0], [0, 0, 0]]
    """
    m[i][j] = x


def list_get_mat(m: list[list[Any]], i: int, j: int) -> Any:
    """Renvoie l'entrée d'une matrice.

    Parameters
    ----------
    m : list
        La matrice à accéder.
    i : int
        L'indice de la ligne à accéder.
    j : int
        L'indice de la colonne à accéder

    Returns
    -------
    float
        La valeur de m à l'indice (i, j).

    Examples
    --------
    >>> m = list_new_mat(2, 3)
    >>> list_set_mat(m, 0, 0, 3)
    >>> list_get_mat(m, 0, 0)
    3
    """
    return m[i][j]
