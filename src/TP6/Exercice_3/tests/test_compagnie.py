import re

import pytest

from ..compagnie import Compagnie


@pytest.mark.parametrize(
    "nom, erreur",
    [
        (["Air France-KLM"], True),
        ({"Air France-KLM"}, True),
        ({"compagnie": "Air France-KLM"}, True),
        (Compagnie("Air France-KLM"), True),
        ("Air France-KLM", False),
        ("Air France", False),
        ("American Airlines", False),
        ("Lufthansa", False),
        ("Norse Atlantic Airways", False),
    ],
)
def test_compagnie_init(nom, erreur):
    if erreur:
        with pytest.raises(TypeError, match=re.escape("Le nom doit être une chaîne de caractères.")):
            Compagnie(nom=nom)
    else:
        compagnie = Compagnie(nom=nom)
        assert compagnie.nom == nom
