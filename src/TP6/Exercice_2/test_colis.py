import re

import pytest

from .colis import Colis


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
            {"poids": 1 + 3j, "mode": "normal"},
            TypeError,
            "'poids' doit être une instance de int ou float.",
        ),
        ({"poids": -42}, ValueError, "'poids' doit être strictement positif."),
        ({"mode": "apide"}, ValueError, "'mode' doit être 'normal' ou 'rapide'."),
        (
            {"volume": "0.28"},
            TypeError,
            "'volume' doit être une instance de int ou float.",
        ),
        ({"volume": -0.28}, ValueError, "'volume' doit être strictement positif."),
    ],
)
def test_init_colis(params, erreur, message_erreur):
    dico = {
        "destination": "Paris",
        "source": "Laval",
        "poids": 42,
        "mode": "normal",
        "volume": 0.28,
    }
    dico.update(**params)
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        Colis(**dico)


@pytest.mark.parametrize(
    "poids, mode, volume, resultat_attendu",
    [
        (42, "normal", 0.56, 0.18),
        (42, "rapide", 0.56, 0.36),
        (42, "normal", 0.58, 0.19),
        (42, "rapide", 0.58, 0.37),
        (45, "normal", 1.24, 0.35),
        (45, "rapide", 1.24, 0.71),
        (342, "normal", 0.378, 0.44),
        (342, "rapide", 0.378, 0.87),
        (1240, "normal", 2.93, 1.97),
        (1240, "rapide", 2.93, 3.95),
        (1240, "normal", 1.6789, 1.66),
        (1240, "rapide", 1.6789, 3.32),
    ],
)
def test_calcul_affranchissement_colis(poids, mode, volume, resultat_attendu):
    assert Colis("P", "L", poids, mode, volume).calcul_affranchissement() == resultat_attendu


@pytest.mark.parametrize(
    "params, resultat_attendu",
    [
        (
            {
                "destination": "Paris",
                "source": "Laval",
                "poids": 42,
                "mode": "normal",
                "volume": 2.48,
            },
            (
                "Colis\n"
                "  Adresse destination : Paris\n"
                "  Adresse expédition : Laval\n"
                "  Poids : 42 grammes\n"
                "  Mode : normal\n"
                "  Volume : 2.48 litres\n"
                "  Prix du timbre : 0.66€"
            ),
        ),
        (
            {
                "destination": "Lorient",
                "source": "Limoges",
                "poids": 1,
                "mode": "rapide",
                "volume": 0.348,
            },
            (
                "Colis\n"
                "  Adresse destination : Lorient\n"
                "  Adresse expédition : Limoges\n"
                "  Poids : 1 gramme\n"
                "  Mode : rapide\n"
                "  Volume : 0.35 litre\n"
                "  Prix du timbre : 0.18€"
            ),
        ),
    ],
)
def test_str_colis(params, resultat_attendu):
    assert str(Colis(**params)) == resultat_attendu
