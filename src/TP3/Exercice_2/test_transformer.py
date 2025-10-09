import pytest

from .transformer import transformer


def puissance(x, n):
    return x**n


def floordiv(x, k):
    return x // k


@pytest.mark.parametrize(
    "fonction, liste, resultat_attendu",
    [
        (lambda x: puissance(x, 2), [1, 2, 4, 8], [1, 4, 16, 64]),
        (lambda x: puissance(x, 3), [1, 2, 4, 8], [1, 8, 64, 512]),
        (lambda x: puissance(x, 3), [1, -1, 1, -1], [1, -1, 1, -1]),
        (lambda x: puissance(x, 4), [1, -1, 1, -1], [1, 1, 1, 1]),
        (lambda x: floordiv(x, 1), [1, 2, 4, 8, 16], [1, 2, 4, 8, 16]),
        (lambda x: floordiv(x, 3), [10, 3, 6, 8, 310], [3, 1, 2, 2, 103]),
        (lambda x: floordiv(x, 5), [10, 3, 4, 8, 310], [2, 0, 0, 1, 62]),
        (lambda x: floordiv(x, 5), [10, 3, 4, 8, 16], [2, 0, 0, 1, 3]),
    ],
)
def test_transformer(fonction, liste, resultat_attendu):
    assert transformer(fonction, liste) == resultat_attendu
