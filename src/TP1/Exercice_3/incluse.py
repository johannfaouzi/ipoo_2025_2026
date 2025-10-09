def incluse(a: str, b: str) -> bool:
    """Vérifie si tous les caractères d'une chaîne sont inclus dans une autre.

    Parameters
    ----------
    a : str
        chaîne avec les caractères à rechercher
    b : str
        chaîne à vérifier

    Returns
    -------
    bool
        True si et seulement si b contient tous les caractères de a.

    Examples
    --------
    >>> incluse('psa', 'abcdpsxyz+-012')
    True
    >>> incluse('', 'abcdpsxyz+-012')
    True
    """
    return all(x in b for x in a)
