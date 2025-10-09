from random import randint
from typing import Any


def permut(liste: list[Any]) -> list[Any]:
    """Permutte aléatoirement les éléments d'une liste.

    Parameters
    ----------
    liste : list
        La liste à permuter.

    Returns
    -------
    list
        La liste permutée.

    Examples
    --------
    >>> liste = [1, 2, 3, 4, 5, 6]
    >>> res = permut(liste)
    >>> isinstance(res, list)
    True
    >>> all(x in liste for x in res)
    True
    >>> len(res) == len(liste)
    True
    """
    indices: list[int] = list(range(len(liste)))
    permut: list[Any] = []
    for _ in range(len(liste)):
        next_idx = randint(0, len(indices) - 1)
        permut.append(indices[next_idx])
        indices = indices[:next_idx] + indices[(next_idx + 1) :]
    return [liste[i] for i in permut]
