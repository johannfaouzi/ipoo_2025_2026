import re

import pytest

from ..passager import Passager


@pytest.mark.parametrize(
    "nom, erreur",
    [
        (["Prénom Nom"], True),
        ({"Prénom Nom"}, True),
        ({"prénom": "Johann", "nom": "Faouzi"}, True),
        (Passager("nom"), True),
        ("nom", False),
        ("nom prénom", False),
        ("prénom nom", False),
        ("Johann Faouzi", False),
    ],
)
def test_aeroport_init(nom, erreur):
    if erreur:
        with pytest.raises(TypeError, match=re.escape("Le nom doit être une chaîne de caractères.")):
            Passager(nom=nom)
    else:
        client = Passager(nom=nom)
        assert client.nom == nom
        assert client.reservations == set()
