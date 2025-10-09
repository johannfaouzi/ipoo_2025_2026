import pytest

from .graphe_set import (
    set_ens_predecesseurs,
    set_ens_puits,
    set_ens_sommets,
    set_ens_sources,
    set_ens_successeurs,
    set_to_dict,
)


@pytest.mark.parametrize(
    "ensemble, resultat_attendu",
    [("graphe_1_set", {"a", "b", "c", "d", "e"}), ("graphe_2_set", {"a", "b", "c"})],
)
def test_set_ens_sommets(ensemble, resultat_attendu, request):
    """Tests pour la fonction set_ens_sommets."""
    graphe = request.getfixturevalue(ensemble)
    assert set_ens_sommets(graphe) == resultat_attendu


@pytest.mark.parametrize(
    "ensemble, sommet, resultat_attendu",
    [
        ("graphe_1_set", "a", {"b"}),
        ("graphe_1_set", "b", {"a", "c", "d", "e"}),
        ("graphe_1_set", "c", {"a", "d"}),
        ("graphe_1_set", "d", {"e"}),
        ("graphe_1_set", "e", set()),
        ("graphe_2_set", "a", {"b", "c"}),
        ("graphe_2_set", "b", {"a", "c"}),
        ("graphe_2_set", "c", {"a", "b"}),
    ],
)
def test_set_ens_successeurs(ensemble, sommet, resultat_attendu, request):
    """Tests pour la fonction set_ens_successeurs."""
    graphe = request.getfixturevalue(ensemble)
    assert set_ens_successeurs(graphe, sommet) == resultat_attendu


@pytest.mark.parametrize(
    "ensemble, sommet, resultat_attendu",
    [
        ("graphe_1_set", "a", {"b", "c"}),
        ("graphe_1_set", "b", {"a"}),
        ("graphe_1_set", "c", {"b"}),
        ("graphe_1_set", "d", {"b", "c"}),
        ("graphe_1_set", "e", {"b", "d"}),
        ("graphe_2_set", "a", {"b", "c"}),
        ("graphe_2_set", "b", {"a", "c"}),
        ("graphe_2_set", "c", {"a", "b"}),
    ],
)
def test_set_ens_predecesseurs(ensemble, sommet, resultat_attendu, request):
    """Tests pour la fonction set_ens_predecesseurs."""
    graphe = request.getfixturevalue(ensemble)
    assert set_ens_predecesseurs(graphe, sommet) == resultat_attendu


@pytest.mark.parametrize(
    "ensemble, resultat_attendu",
    [
        ("graphe_1_set", {"e"}),
        ("graphe_2_set", set()),
    ],
)
def test_set_ens_puits(ensemble, resultat_attendu, request):
    """Tests pour la fonction set_ens_puits."""
    graphe = request.getfixturevalue(ensemble)
    assert set_ens_puits(graphe) == resultat_attendu


@pytest.mark.parametrize(
    "ensemble, resultat_attendu",
    [
        ("graphe_1_set", set()),
        ("graphe_2_set", set()),
    ],
)
def test_set_ens_sources(ensemble, resultat_attendu, request):
    """Tests pour la fonction set_ens_sources."""
    graphe = request.getfixturevalue(ensemble)
    assert set_ens_sources(graphe) == resultat_attendu


@pytest.mark.parametrize(
    "ensemble, resultat_attendu",
    [("graphe_1_set", "graphe_1_dict"), ("graphe_2_set", "graphe_2_dict")],
)
def test_graphe(ensemble, resultat_attendu, request):
    graphe_ens = request.getfixturevalue(ensemble)
    graphe_dict = request.getfixturevalue(resultat_attendu)
    assert set_to_dict(graphe_ens) == graphe_dict
