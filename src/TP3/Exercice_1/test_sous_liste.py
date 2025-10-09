import pytest

from .sous_liste import sous_liste


@pytest.mark.parametrize(
    "petite_liste, grande_liste, resultat_attendu",
    [
        ([0, 2, 4], [0, 1, 2, 3, 4, 5], True),
        ([2, 0, 4], [0, 1, 2, 3, 4, 5], False),
        ([2, 4], [0, 1, 2, 3, 4, 5], True),
        ([2, 0, 4], [2, 0, 1, 2, 3, 4, 5], True),
        ([7, 0, 4], [0, 1, 2, 3, 4, 5], False),
        ([0, 7, 4], [0, 1, 2, 3, 4, 5], False),
        ([0, 4, 7], [0, 1, 2, 3, 4, 5], False),
        ([2, 4, 6, 5], [2, 1, 4, 3, 6, 5], True),
        ([2, 1, 4, 3, 6, 5], [2, 1, 4, 3, 6, 5], True),
        ([2, 1, 4, 3, 6, 5, 2], [2, 1, 4, 3, 6, 5], False),
    ],
)
def test_sous_liste(petite_liste, grande_liste, resultat_attendu):
    assert sous_liste(petite_liste, grande_liste) == resultat_attendu
