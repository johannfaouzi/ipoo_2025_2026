""""Exemples de graphes pour les tests."""

import pytest


# Graphe 1
@pytest.fixture
def graphe_1_dict():
    return {"a": {"b"}, "b": {"a", "c", "d", "e"}, "c": {"a", "d"}, "d": {"e"}, "e": set()}


@pytest.fixture
def graphe_1_set():
    return {("a", "b"), ("b", "a"), ("c", "a"), ("c", "d"), ("b", "c"), ("b", "d"), ("b", "e"), ("d", "e")}


# Graphe 2
@pytest.fixture
def graphe_2_dict():
    return {"a": {"b", "c"}, "b": {"a", "c"}, "c": {"a", "b"}}


@pytest.fixture
def graphe_2_set():
    return {("a", "b"), ("a", "c"), ("b", "a"), ("b", "c"), ("c", "a"), ("c", "b")}
