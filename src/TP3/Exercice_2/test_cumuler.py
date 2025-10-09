import pytest

from .cumuler import cumuler


def somme(x, y):
    return x + y


def produit(x, y):
    return x * y


@pytest.mark.parametrize(
    "fonction, liste, resultat_attendu",
    [
        (somme, [1, 2, 4], 7),
        (somme, [1, 2, 4, 8], 15),
        (somme, [1, 2, 4, -1, -2, -4], 0),
        (produit, [1, 2, 4], 8),
        (produit, [1, 2, 4, 8], 64),
        (produit, [1, 2, 4, -1, -2, -4], -64),
        (produit, [1, 2, 4, -1, -2, -4, 0], 0),
        (produit, [0, 1, 2, 4, -1, -2, -4], 0),
    ],
)
def test_cumuler(fonction, liste, resultat_attendu):
    assert cumuler(fonction, liste) == resultat_attendu
