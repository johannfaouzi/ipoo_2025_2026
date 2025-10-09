import pytest

from .mat_list import list_get_mat, list_new_mat, list_set_mat


@pytest.fixture
def matrix():
    return [
        [0, 1, 2, 3, 4],
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6],
    ]


@pytest.mark.parametrize(
    "nl, nc, resultat_attendu",
    [
        (1, 1, [[0]]),
        (1, 3, [[0, 0, 0]]),
        (3, 1, [[0], [0], [0]]),
        (2, 3, [[0, 0, 0], [0, 0, 0]]),
        (3, 2, [[0, 0], [0, 0], [0, 0]]),
        (3, 3, [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
    ],
)
def test_list_new_mat(nl, nc, resultat_attendu):
    """Tests pour la fonction list_new_mat."""
    assert list_new_mat(nl, nc) == resultat_attendu


@pytest.mark.parametrize(
    "i, j, x, resultat_attendu",
    [
        (0, 0, 23, [[23, 1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]),
        (2, 1, 123, [[0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 123, 4, 5, 6]]),
        (1, 3, 234, [[0, 1, 2, 3, 4], [1, 2, 3, 234, 5], [2, 3, 4, 5, 6]]),
        (0, -1, -2, [[0, 1, 2, 3, -2], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]),
    ],
)
def test_list_set_mat(matrix, i, j, x, resultat_attendu):
    """Tests pour la fonction list_set_mat."""
    list_set_mat(matrix, i, j, x)
    assert matrix == resultat_attendu


@pytest.mark.parametrize(
    "i, j, resultat_attendu",
    [
        (0, 0, 0),
        (1, 0, 1),
        (0, 1, 1),
        (0, 4, 4),
        (1, 4, 5),
        (2, 4, 6),
    ],
)
def test_list_get_mat(matrix, i, j, resultat_attendu):
    """Tests pour la fonction list_get_mat."""
    assert list_get_mat(matrix, i, j) == resultat_attendu
