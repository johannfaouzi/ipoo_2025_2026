import pytest

from .filtrer import filtrer


def est_divisible_par(n, k):
    return n % k == 0


@pytest.mark.parametrize(
    "fonction, liste, resultat_attendu",
    [
        (lambda n: est_divisible_par(n, 2), [1, 2, 4, 8, 16], [2, 4, 8, 16]),
        (lambda n: est_divisible_par(n, 2), [3, 1, -2, 7, 11], [-2]),
        (lambda n: est_divisible_par(n, 3), [1, 2, 4, 8, 16], []),
        (lambda n: est_divisible_par(n, 4), [1, 2, 4, 8, 16], [4, 8, 16]),
        (lambda n: est_divisible_par(n, 5), [1, 2, 4, 8, 16], []),
        (lambda n: est_divisible_par(n, 6), [1, 2, 4, 8, 16], []),
        (lambda n: est_divisible_par(n, 2), list(range(300)), list(range(0, 300, 2))),
        (lambda n: est_divisible_par(n, 3), list(range(100)), list(range(0, 100, 3))),
        (
            lambda n: est_divisible_par(n, 4),
            list(range(-100, 100)),
            list(range(-100, 100, 4)),
        ),
    ],
)
def test_filtrer(fonction, liste, resultat_attendu):
    assert filtrer(fonction, liste) == resultat_attendu
