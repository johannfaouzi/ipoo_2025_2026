def dict_ens_sommets(graphe: dict[str, set[str]]) -> set[str]:
    """Ensemble des sommets d'un graphe

    Implémentation par ensemble d'arcs.

    Parameters
    ----------
    graphe : dict
        Dictionnaire du graphe.

    Returns
    -------
    set
        Ensemble des étiquettes des sommets.

    Examples
    --------
    >>> g = {'a': {'b'},
    ...      'b': {'a', 'c', 'd', 'e'},
    ...      'c': {'a', 'd'},
    ...      'd': {'e'},
    ...      'e': set()}
    >>> s = dict_ens_sommets(g)
    >>> isinstance(s, set)
    True
    >>> sorted(list(s))
    ['a', 'b', 'c', 'd', 'e']
    """
    return set(graphe.keys())


def dict_ens_successeurs(graphe: dict[str, set[str]], sommet: str) -> set[str]:
    """Ensemble des successeurs d'un nœud d'un graphe.

    Implémentation par ensemble d'arcs.

    Parameters
    ----------
    graphe : dict
        Dictionnaire du graphe.
    sommet
        Sommet d'origine.

    Returns
    -------
    set
        Ensemble des étiquettes des successeurs du sommet.

    Examples
    --------
    >>> g = {'a': {'b'},
    ...      'b': {'a', 'c', 'd', 'e'},
    ...      'c': {'a', 'd'},
    ...      'd': {'e'},
    ...      'e': set()}
    >>> s = dict_ens_successeurs(g, 'a')
    >>> isinstance(s, set)
    True
    >>> list(s)
    ['b']
    """
    return set(graphe[sommet])


def dict_ens_predecesseurs(graphe: dict[str, set[str]], sommet: str) -> set[str]:
    """Ensemble des prédecesseurs d'un sommet d'un graphe.

    Implémentation par ensemble d'arcs.

    Parameters
    ----------
    graphe : dict
        Dictionnaire du graphe.
    sommet
        Sommet d'origine.

    Returns
    -------
    set
        Ensemble des étiquettes des sommets prédecesseurs du sommet.

    Examples
    --------
    >>> g = {'a': {'b'},
    ...      'b': {'a', 'c', 'd', 'e'},
    ...      'c': {'a', 'd'},
    ...      'd': {'e'},
    ...      'e': set()}
    >>> s = dict_ens_predecesseurs(g, 'e')
    >>> isinstance(s, set)
    True
    >>> sorted(list(s))
    ['b', 'd']
    """
    return {key for key, value in graphe.items() if sommet in value}


def dict_ens_puits(graphe: dict[str, set[str]]) -> set[str]:
    """Ensemble des puits d'un graphe.

    Implémentation par dictionnaire.

    Parameters
    ----------
    graphe : dict
        Dictionnaire du graphe.

    Returns
    -------
    set
        Ensemble des étiquettes des puits du graphe.

    Examples
    --------
    >>> g = {'a': {'b'},
    ...      'b': {'a', 'c', 'd', 'e'},
    ...      'c': {'a', 'd'},
    ...      'd': {'e'},
    ...      'e': set()}
    >>> s = dict_ens_puits(g)
    >>> isinstance(s, set)
    True
    >>> sorted(list(s))
    ['e']
    """
    return {key for key, value in graphe.items() if len(value) == 0}


def dict_ens_sources(graphe: dict[str, set[str]]) -> set[str]:
    """Ensemble des sources d'un graphe.

    Implémentation par liste d'adjacences.

    Parameters
    ----------
    graphe : dict
        Dictionnaire du graphe.

    Returns
    -------
    set
        Ensemble des étiquettes des sommets source d'un arc.

    Examples
    --------
    >>> g = {'a': {'b'},
    ...      'b': {'a', 'c', 'd', 'e'},
    ...      'c': {'a', 'd'},
    ...      'd': {'e'},
    ...      'e': set()}
    >>> s = dict_ens_sources(g)
    >>> isinstance(s, set)
    True
    >>> s
    set()
    """
    res = set(graphe.keys())
    for value in graphe.values():
        res = res.difference(value)
    return res


def dict_to_set(graphe: dict[str, set[str]]) -> set[tuple[str, str]]:
    """Conversion d'un dictionnaire en un ensemble d'arcs.

    Parameters
    ----------
    graphe : dict
        Dictionnaire représentant le graphe.

    Returns
    -------
    set
        Graphe sous forme d'ensemble d'arcs.

    Examples
    --------
    >>> g = {'a': {'b'},
    ...      'b': {'a', 'c', 'd', 'e'},
    ...      'c': {'a', 'd'},
    ...      'd': {'e'},
    ...      'e': set()}
    >>> g_new = dict_to_set(g)
    >>> ('a', 'b') in g_new
    True
    >>> ('b', 'd') in g_new
    True
    """
    return {(key, val) for key, value in graphe.items() for val in value}
