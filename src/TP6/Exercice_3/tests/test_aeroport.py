import re

import pytest

from ..aeroport import Aeroport


@pytest.mark.parametrize(
    "kwargs, message_erreur",
    [
        (
            {"nom": ["Paris-CDG"], "ville": ["Paris"]},
            "Le nom doit être une chaîne de caractères.",
        ),
        (
            {"nom": ["Paris-CDG"], "ville": "Paris"},
            "Le nom doit être une chaîne de caractères.",
        ),
        (
            {"nom": {"Paris-CDG"}, "ville": ["Paris"]},
            "Le nom doit être une chaîne de caractères.",
        ),
        (
            {"nom": "Paris-CDG", "ville": ["Paris"]},
            "La ville doit être une chaîne de caractères.",
        ),
        (
            {"nom": "Paris-CDG", "ville": ("Paris",)},
            "La ville doit être une chaîne de caractères.",
        ),
        ({"nom": "Aéroport de Paris-Charles-de-Gaulle", "ville": "Paris"}, None),
        ({"nom": "Aéroport Rennes Bretagne", "ville": "Rennes"}, None),
        ({"nom": "Aéroport Nantes Atlantique", "ville": "Nantes"}, None),
        ({"nom": "Aéroport de Lyon-Saint-Exupéry", "ville": "Lyon"}, None),
        ({"nom": "Aéroport de Limoges-Bellegarde", "ville": "Limoges"}, None),
    ],
)
def test_aeroport_init(kwargs, message_erreur):
    if message_erreur:
        with pytest.raises(TypeError, match=re.escape(message_erreur)):
            Aeroport(**kwargs)
    else:
        aeroport = Aeroport(**kwargs)
        assert aeroport.nom == kwargs["nom"]
        assert aeroport.ville == kwargs["ville"]
