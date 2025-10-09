import re

import pytest

from .lettre import Lettre


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
            {"format_lettre": "A5"},
            ValueError,
            "'format_lettre' doit être 'A3' ou 'A4'.",
        ),
    ],
)
def test_init_lettre(params, erreur, message_erreur):
    dico = {
        "destination": "Paris",
        "source": "Laval",
        "poids": 42,
        "mode": "normal",
        "format_lettre": "A4",
    }
    dico.update(**params)
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        Lettre(**dico)


@pytest.mark.parametrize(
    "poids, mode, format_lettre, resultat_attendu",
    [
        (42, "normal", "A4", 2.54),
        (42, "rapide", "A4", 5.08),
        (42, "normal", "A3", 3.54),
        (42, "rapide", "A3", 7.08),
        (45, "normal", "A4", 2.54),
        (45, "rapide", "A4", 5.09),
        (342, "normal", "A4", 2.84),
        (342, "rapide", "A4", 5.68),
        (1240, "normal", "A4", 3.74),
        (1240, "rapide", "A4", 7.48),
        (1240, "normal", "A3", 4.74),
        (1240, "rapide", "A3", 9.48),
    ],
)
def test_calcul_affranchissement_lettre(poids, mode, format_lettre, resultat_attendu):
    assert Lettre("P", "L", poids, mode, format_lettre).calcul_affranchissement() == resultat_attendu


@pytest.mark.parametrize(
    "params, resultat_attendu",
    [
        (
            {
                "destination": "Paris",
                "source": "Laval",
                "poids": 42,
                "mode": "normal",
                "format_lettre": "A4",
            },
            (
                "Lettre\n"
                "  Adresse destination : Paris\n"
                "  Adresse expédition : Laval\n"
                "  Poids : 42 grammes\n"
                "  Mode : normal\n"
                "  Format : A4\n"
                "  Prix du timbre : 2.54€"
            ),
        ),
        (
            {
                "destination": "Lorient",
                "source": "Limoges",
                "poids": 1,
                "mode": "rapide",
                "format_lettre": "A3",
            },
            (
                "Lettre\n"
                "  Adresse destination : Lorient\n"
                "  Adresse expédition : Limoges\n"
                "  Poids : 1 gramme\n"
                "  Mode : rapide\n"
                "  Format : A3\n"
                "  Prix du timbre : 7.00€"
            ),
        ),
    ],
)
def test_str_lettre(params, resultat_attendu):
    assert str(Lettre(**params)) == resultat_attendu
