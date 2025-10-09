from random import randint


def frequence_int(n: int, a: int, b: int) -> dict[int, float]:
    """Calcule le nombre d'occurence de chaque entier tiré par randint()

    Parameters
    ----------
    n : int
        Nombre d'échantillons à tirer
    a : int
        Borne inférieure
    b : int
        Borne supérieure

    Returns
    -------
    dict[int, float]
        Proportions des entiers.

    Examples
    --------
    >>> freq = frequence_int(100_000, 0, 5)
    >>> freq
    {0: 0.1..., 1: 0.1..., 2: 0.1..., 3: 0.1..., 4: 0.1..., 5: 0.1...}
    >>> (max(freq.values()) - min(freq.values())) < 1e-2
    True
    """
    liste: list[int] = [randint(a, b) for _ in range(n)]
    return dict((i, liste.count(i) / n) for i in range(a, b + 1))
