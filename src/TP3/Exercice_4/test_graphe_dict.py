import pytest

from .graphe_dict import (
    dict_ens_predecesseurs,
    dict_ens_puits,
    dict_ens_sommets,
    dict_ens_sources,
    dict_ens_successeurs,
    dict_to_set,
)


@pytest.mark.parametrize(
    "dico, resultat_attendu",
    [("graphe_1_dict", {"a", "b", "c", "d", "e"}), ("graphe_2_dict", {"a", "b", "c"})],
)
def test_dict_ens_sommets(dico, resultat_attendu, request):
    """Tests pour la fonction dict_ens_sommets."""
    graphe = request.getfixturevalue(dico)
    assert dict_ens_sommets(graphe) == resultat_attendu


@pytest.mark.parametrize(
    "dico, sommet, resultat_attendu",
    [
        ("graphe_1_dict", "a", {"b"}),
        ("graphe_1_dict", "b", {"a", "c", "d", "e"}),
        ("graphe_1_dict", "c", {"a", "d"}),
        ("graphe_1_dict", "d", {"e"}),
        ("graphe_1_dict", "e", set()),
        ("graphe_2_dict", "a", {"b", "c"}),
        ("graphe_2_dict", "b", {"a", "c"}),
        ("graphe_2_dict", "c", {"a", "b"}),
    ],
)
def test_dict_ens_successeurs(dico, sommet, resultat_attendu, request):
    """Tests pour la fonction dict_ens_successeurs."""
    graphe = request.getfixturevalue(dico)
    assert dict_ens_successeurs(graphe, sommet) == resultat_attendu


@pytest.mark.parametrize(
    "dico, sommet, resultat_attendu",
    [
        ("graphe_1_dict", "a", {"b", "c"}),
        ("graphe_1_dict", "b", {"a"}),
        ("graphe_1_dict", "c", {"b"}),
        ("graphe_1_dict", "d", {"b", "c"}),
        ("graphe_1_dict", "e", {"b", "d"}),
        ("graphe_2_dict", "a", {"b", "c"}),
        ("graphe_2_dict", "b", {"a", "c"}),
        ("graphe_2_dict", "c", {"a", "b"}),
    ],
)
def test_dict_ens_predecesseurs(dico, sommet, resultat_attendu, request):
    """Tests pour la fonction dict_ens_predecesseurs."""
    graphe = request.getfixturevalue(dico)
    assert dict_ens_predecesseurs(graphe, sommet) == resultat_attendu


@pytest.mark.parametrize(
    "dico, resultat_attendu",
    [
        ("graphe_1_dict", {"e"}),
        ("graphe_2_dict", set()),
    ],
)
def test_dict_ens_puits(dico, resultat_attendu, request):
    """Tests pour la fonction dict_ens_puits."""
    graphe = request.getfixturevalue(dico)
    assert dict_ens_puits(graphe) == resultat_attendu


@pytest.mark.parametrize(
    "dico, resultat_attendu",
    [
        ("graphe_1_dict", set()),
        ("graphe_2_dict", set()),
    ],
)
def test_dict_ens_sources(dico, resultat_attendu, request):
    """Tests pour la fonction dict_ens_sources."""
    graphe = request.getfixturevalue(dico)
    assert dict_ens_sources(graphe) == resultat_attendu


@pytest.mark.parametrize(
    "dico, resultat_attendu",
    [("graphe_1_dict", "graphe_1_set"), ("graphe_2_dict", "graphe_2_set")],
)
def test_ensemble_arcs(dico, resultat_attendu, request):
    graphe_dict = request.getfixturevalue(dico)
    graphe_set = request.getfixturevalue(resultat_attendu)
    assert dict_to_set(graphe_dict) == graphe_set
