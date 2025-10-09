from typing import Any


def dict_new_mat(nl: int, nc: int) -> dict[tuple[int, int], Any]:
    """Crée une nouvelle matrice vide sous forme de dictionnaire.

    Une matrice vide n'est constitutée que de zéros.

    Parameters
    ----------
    nl : int
        Nombre de lignes.
    nc : int
        Nombre de colonnes.

    Returns
    -------
    dict
        Dictionnaire vide représentant la matrice.

    Examples
    --------
    >>> dict_new_mat(2, 3)
    {}
    """
    return {}


def dict_set_mat(m: dict[tuple[int, int], Any], i: int, j: int, x: Any) -> None:
    """Change une entrée d'une matrice

    Parameters
    ----------
    m : dict
        La matrice à modifier.
    i : int
        L'indice de la ligne à modifier
    j : int
        L'indice de la colonne à modifier
    x
        La nouvelle valeur.

    Examples
    --------
    >>> m = dict_new_mat(2, 3)
    >>> dict_set_mat(m, 0, 0, 3)
    >>> m
    {(0, 0): 3}
    """
    m[(i, j)] = x


def dict_get_mat(m: dict[tuple[int, int], Any], i: int, j: int) -> Any:
    """Accède à une entrée d'une matrice

    Parameters
    ----------
    m : dict
        La matrice à accéder.
    i : int
        L'indice de la ligne à modifier.
    j : int
        L'indice de la colonne à modifier.

    Returns
    -------
    float
        La valeur de m à l'indice (i, j).

    Examples
    --------
    >>> m = dict_new_mat(2, 3)
    >>> dict_set_mat(m, 0, 0, 3)
    >>> dict_get_mat(m, 0, 0)
    3
    """
    if (i, j) not in m:
        return 0
    return m[(i, j)]
