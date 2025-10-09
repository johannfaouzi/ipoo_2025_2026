from typing import Any


def fusion_v1(list1: list[Any], list2: list[Any]) -> list[Any]:
    """Fusionne deux listes et renvoie une liste triée sans doublons.

    Parameters
    ----------
    list1 : list
        Liste de valeurs triées et sans doublon
    list2 : list
        Liste de valeurs triées et sans doublon

    Returns
    -------
    list
        La liste triées sans doublon fusionnée

    Examples
    --------
    >>> fusion_v1([1, 2, 3, 7, 11], [2, 3, 6, 10])
    [1, 2, 3, 6, 7, 10, 11]
    """
    return sorted(list(set(list1 + list2)))


def fusion_v2(list1: list[Any], list2: list[Any]) -> list[Any]:
    """Fusionne deux listes et renvoie une liste triée sans doublons.

    Parameters
    ----------
    list1 : list
        Liste de valeurs triées et sans doublon.
    list2 : list
        Liste de valeurs triées et sans doublon.

    Returns
    -------
    list
        La liste triées sans doublon fusionnée

    Examples
    --------
    >>> fusion_v2([1, 2, 3, 7, 11], [2, 3, 6, 10])
    [1, 2, 3, 6, 7, 10, 11]

    """
    res: list[Any] = []
    idx1: int = 0
    idx2: int = 0
    len1: int = len(list1)
    len2: int = len(list2)

    while idx1 < len1:
        if idx2 < len2:
            x: Any = min(list1[idx1], list2[idx2])
            res.append(x)
            if x in list1:
                idx1 += 1
            if x in list2:
                idx2 += 1
        else:
            res.extend(list1[idx1:])
            idx1 = len1

    if idx2 < len2:
        res.extend(list2[idx2:])

    return res
