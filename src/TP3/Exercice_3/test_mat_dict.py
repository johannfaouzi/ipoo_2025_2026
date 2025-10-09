import pytest

from .mat_dict import dict_get_mat, dict_new_mat, dict_set_mat


@pytest.fixture
def matrix():
    return {(0, 0): 2, (0, 1): 1, (0, 3): 6, (1, 2): 4, (2, 0): 3, (2, 3): 9}


@pytest.mark.parametrize("nl, nc", [(1, 1), (1, 2), (2, 1), (2, 2), (42, 3), (11, 123), (7, 11), (9, 17)])
def test_dict_new_mat(nl, nc):
    """Tests pour la fonction list_new_mat."""
    assert dict_new_mat(nl, nc) == {}


@pytest.mark.parametrize(
    "i, j, x, resultat_attendu",
    [
        (0, 0, 23, {(0, 0): 23, (0, 1): 1, (0, 3): 6, (1, 2): 4, (2, 0): 3, (2, 3): 9}),
        (
            0,
            3,
            "abc",
            {(0, 0): 2, (0, 1): 1, (0, 3): "abc", (1, 2): 4, (2, 0): 3, (2, 3): 9},
        ),
        (
            0,
            2,
            "02",
            {
                (0, 0): 2,
                (0, 1): 1,
                (0, 3): 6,
                (1, 2): 4,
                (2, 0): 3,
                (2, 3): 9,
                (0, 2): "02",
            },
        ),
        (
            2,
            1,
            42,
            {
                (0, 0): 2,
                (0, 1): 1,
                (0, 3): 6,
                (1, 2): 4,
                (2, 0): 3,
                (2, 3): 9,
                (2, 1): 42,
            },
        ),
    ],
)
def test_dict_set_mat(matrix, i, j, x, resultat_attendu):
    """Tests pour la fonction list_set_mat."""
    dict_set_mat(matrix, i, j, x)
    assert matrix == resultat_attendu


@pytest.mark.parametrize(
    "i, j, resultat_attendu",
    [
        (0, 0, 2),
        (1, 0, 0),
        (0, 1, 1),
        (0, 3, 6),
        (1, 1, 0),
        (2, 3, 9),
    ],
)
def test_dict_get_mat(matrix, i, j, resultat_attendu):
    """Tests pour la fonction list_get_mat."""
    assert dict_get_mat(matrix, i, j) == resultat_attendu
