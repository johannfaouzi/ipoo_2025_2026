import re
from unittest.mock import patch

import pytest

from .courrier import Courrier


@pytest.fixture
def dico_kwargs():
    return {"destination": "Paris", "source": "Laval", "poids": 42, "mode": "normal"}


@pytest.mark.parametrize(
    "params, erreur, message_erreur",
    [
        (
            {"destination": ["Paris"]},
            TypeError,
            "'destination' doit être une instance de str.",
        ),
        ({"source": {"Laval"}}, TypeError, "'source' doit être une instance de str."),
        (
            {"poids": 1 + 3j},
            TypeError,
            "'poids' doit être une instance de int ou float.",
        ),
        ({"poids": -42}, ValueError, "'poids' doit être strictement positif."),
        ({"mode": "apide"}, ValueError, "'mode' doit être 'normal' ou 'rapide'."),
    ],
)
@patch.multiple(Courrier, __abstractmethods__=set())
def test_init_courrier(dico_kwargs, params, erreur, message_erreur):
    dico_kwargs.update(**params)
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        Courrier(**dico_kwargs)
