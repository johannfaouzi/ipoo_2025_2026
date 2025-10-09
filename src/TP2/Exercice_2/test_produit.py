import re

import pytest

from .produit import produit


@pytest.mark.parametrize(
    "liste, message_erreur",
    [
        ({1, 2, 3}, "liste doit être une liste"),
        ((1, 2, 4), "liste doit être une liste"),
        (
            [1, 2.0, 3],
            "Tous les éléments de la liste doivent être des entiers " "(2.0 n'est pas un entier)",
        ),
        (
            [1, 2, "3"],
            "Tous les éléments de la liste doivent être des entiers " "('3' n'est pas un entier)",
        ),
        (
            [[1], 2, 3],
            "Tous les éléments de la liste doivent être des entiers " "([1] n'est pas un entier)",
        ),
    ],
)
def test_erreur_produit(liste, message_erreur):
    with pytest.raises(TypeError, match=re.escape(message_erreur)):
        produit(liste)


@pytest.mark.parametrize(
    "liste, resultat_attendu",
    [
        ([], 1),
        ([1], 1),
        ([2], 2),
        ([1, 2], 2),
        ([2, 3, 4], 24),
        ([-3, 6, 5], -90),
        ([0, 2, 4, 7, 12], 0),
        ([12, 12], 144),
        ([3, 3, 3], 27),
        ([2, 2, 2, 2, 2, 2], 64),
        ([1, 2, 3, 4, 5, 6], 720),
        ([1, -2, 3, -4, 5, -6], -720),
    ],
)
def test_resultat_produit(liste, resultat_attendu):
    assert produit(liste) == resultat_attendu
