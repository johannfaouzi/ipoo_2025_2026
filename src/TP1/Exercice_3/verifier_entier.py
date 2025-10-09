from .incluse import incluse


def verifier_entier_valide(val: str, inf: int | None, sup: int | None) -> bool:
    """Vérifie qu'une chaîne représente un entier dans un interval.

    Parameters
    ----------
    val : str
        chaîne à vérifier
    inf : int | None
        borne inférieure (ou None si il n'y en a pas)
    sup : int | None
        borne supérieure (ou None si il n'y en a pas)

    Returns
    -------
    bool
        True si et seulement si val est un entier entre inf et sup

    Examples
    --------
    >>> verifier_entier_valide('123a', None, None)
    False

    >>> verifier_entier_valide('123', None, None)
    True

    >>> verifier_entier_valide('123', 1, 100)
    False

    >>> verifier_entier_valide('0123', 1, 200)
    True

    >>> verifier_entier_valide('', None, None)
    False
    """
    # Python, comme beacoup de langages, effectue une évaluation paresseuse
    # de la condition ci-dessous, à savoir, si la première condition dans un
    # "et logique" (and) est fausse, la deuxième n'est pas évaluée.
    # Ici, si elle l'était, int(...) reverrai une erreur.
    if len(val):
        return incluse(val, "0123456789") and (inf is None or int(val) >= inf) and (sup is None or int(val) <= sup)
    else:
        return False
