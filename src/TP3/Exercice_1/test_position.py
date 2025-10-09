import pytest

from .position import position


@pytest.mark.parametrize(
    "elt, liste, depart, resultat_attendu",
    [
        (0, [1, 2, 4, 8], 0, -1),
        (1, [1, 2, 4, 8], 0, 0),
        (2, [1, 2, 4, 8], 0, 1),
        (1, [1, 2, 4, 8], 1, -1),
        (1, [1, 2, 4, 8], 1, -1),
        (2, [1, 2, 4, 8], 2, -1),
        (2, [1, 2, 4, 8], 6, -1),
    ],
)
def test_position(elt, liste, depart, resultat_attendu):
    assert position(elt, liste, depart) == resultat_attendu
