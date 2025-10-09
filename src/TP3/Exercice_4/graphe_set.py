def set_ens_sommets(set_arcs: set[tuple[str, str]]) -> set[str]:
    """Ensemble des sommets d'un graphe.

    Implémentation par ensemble d'arcs.

    Parameters
    ----------
    set_arcs : set
        Ensemble des arcs du graphe

    Returns
    -------
    set
        ensemble des étiquettes des sommets

    Examples
    --------
    >>> g = {('a', 'b'), ('b', 'a'), ('c', 'a'), ('c', 'd'),
    ...      ('b', 'c'), ('b', 'd'), ('b', 'e'), ('d', 'e')}
    >>> s = set_ens_sommets(g)
    >>> isinstance(s, set)
    True
    >>> sorted(list(s))
    ['a', 'b', 'c', 'd', 'e']
    """
    # Solution possible : transformer chaque tuple en ensemble puis faire
    # l'union de tous les ensembles :
    # set().union(*[set(arc) for arc in set_arcs])

    # Autre solution possible : créer l'ensemble des premiers éléments des
    # tuples et faire l'union avec l'ensemble des seconds éléments des tuples.
    return {arc[0] for arc in set_arcs}.union({arc[1] for arc in set_arcs})


def set_ens_successeurs(set_arcs: set[tuple[str, str]], n: str) -> set[str]:
    """Ensemble des successeurs d'un nœud d'un graphe.

    Implémentation par ensemble d'arcs.

    Parameters
    ----------
    set_arcs : list
        Liste des arcs du graphe.
    n
        Nœud d'origine des arcs.

    Returns
    -------
    set
        Ensemble des sommets successeurs d'un arc.

    Examples
    --------
    >>> g = {('a', 'b'), ('b', 'a'), ('c', 'a'), ('c', 'd'),
    ...      ('b', 'c'), ('b', 'd'), ('b', 'e'), ('d', 'e')}
    >>> s = set_ens_successeurs(g, 'a')
    >>> isinstance(s, set)
    True
    >>> sorted(list(s))
    ['b']
    """
    return {e for (o, e) in set_arcs if o == n}


def set_ens_predecesseurs(set_arcs: set[tuple[str, str]], n: str) -> set[str]:
    """Ensemble des prédecesseurs des nœuds d'un graphe

    Implémentation par ensemble d'arcs.

    Parameters
    ----------
    set_arcs : set
        Ensemble des arcs du graphe.
    n
        Nœud d'origine des arcs.

    Returns
    -------
    set
        Ensemble des sommets successeurs d'un arc.

    Examples
    --------
    >>> g = {('a', 'b'), ('b', 'a'), ('c', 'a'), ('c', 'd'),
    ...      ('b', 'c'), ('b', 'd'), ('b', 'e'), ('d', 'e')}
    >>> s = set_ens_predecesseurs(g, 'a')
    >>> isinstance(s, set)
    True
    >>> sorted(list(s))
    ['b', 'c']
    """
    return {o for (o, e) in set_arcs if e == n}


def set_ens_puits(set_arcs: set[tuple[str, str]]) -> set[str]:
    """Ensemble des puits d'un graphe

    Implémentation par ensemble d'arcs.

    Parameters
    ----------
    set_arcs : list
        Liste des arcs du graphe.

    Returns
    -------
    set
        Ensemble des étiquettes des puits du graphe.

    Examples
    --------
    >>> g = {('a', 'b'), ('b', 'a'), ('c', 'a'), ('c', 'd'),
    ...      ('b', 'c'), ('b', 'd'), ('b', 'e'), ('d', 'e')}
    >>> s = set_ens_puits(g)
    >>> isinstance(s, set)
    True
    >>> sorted(list(s))
    ['e']
    """
    return {arc[1] for arc in set_arcs}.difference({arc[0] for arc in set_arcs})


def set_ens_sources(set_arcs: set[tuple[str, str]]) -> set[str]:
    """Ensemble des puits d'un graphe

    Implémentation par ensemble d'arcs.

    Parameters
    ----------
    set_arcs : set
        Ensemble des arcs du graphe.

    Returns
    -------
    set
        Ensemble des étiquettes des puits du graphe.

    Examples
    --------
    >>> g = {('a', 'b'), ('b', 'a'), ('c', 'a'), ('c', 'd'),
    ...      ('b', 'c'), ('b', 'd'), ('b', 'e'), ('d', 'e')}
    >>> s = set_ens_sources(g)
    >>> isinstance(s, set)
    True
    >>> sorted(list(s))
    []
    """
    return {o for o, _ in set_arcs}.difference({e for _, e in set_arcs})


def set_to_dict(set_arcs: set[tuple[str, str]]) -> dict[str, set[str]]:
    """Conversion d'un ensemble d'arcs en un dictionnaire.

    Parameters
    ----------
    set_arcs : ensemble
        Ensemble des arcs du graphe.

    Returns
    -------
    dict
        Graphe sous forme de dictionnaire.

    Examples
    --------
    >>> g = {('a', 'b'), ('b', 'a'), ('c', 'a'), ('c', 'd'),
    ...       ('b', 'c'), ('b', 'd'), ('b', 'e'), ('d', 'e')}
    >>> g_new = set_to_dict(g)
    >>> sorted(g_new.keys())
    ['a', 'b', 'c', 'd', 'e']
    >>> g_new['a']
    {'b'}
    >>> g_new['e']
    set()
    """
    g: dict[str, set[str]] = {s: set() for s in set_ens_sommets(set_arcs)}
    for o, e in set_arcs:
        g[o].add(e)
    return g
