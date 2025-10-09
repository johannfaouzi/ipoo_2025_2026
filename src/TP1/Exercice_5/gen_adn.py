from random import randint


def gen_adn(n: int) -> str:
    """Génère une séquence ADN aléatoire.

    Parameters
    ----------
    n : int
        Longueur de la chaîne.

    Returns
    -------
    list
        La chaîne ADN générée.

    Examples
    --------
    >>> res = gen_adn(30)
    >>> isinstance(res, str)
    True
    >>> set(res) == {'A', 'C', 'G', 'T'}
    True
    >>> len(res) == 30
    True
    """
    mapping: dict[int, str] = {0: "A", 1: "C", 2: "G", 3: "T"}
    return "".join(mapping[randint(0, 3)] for _ in range(n))
