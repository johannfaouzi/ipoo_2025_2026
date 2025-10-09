"""Tests pour les fonctions de validation des questionnaires."""

import datetime
import re

import pytest

from .questionnaire import valider_questionnaire, valider_questionnaire_str


@pytest.fixture
def dico():
    return {
        "nom": "Faouzi",
        "prenom": "Johann",
        "date_naissance": datetime.date(1993, 6, 21),
        "adresse_numero": 42,
        "adresse_rue": "Rue aléatoire",
        "adresse_ville": "Rennes",
        "adresse_code_postal": "35000",
        "telephone": "0612345678",
        "age_minimum": None,
    }


@pytest.fixture
def dico_str():
    return {
        "nom": "Faouzi",
        "prenom": "Johann",
        "date_naissance": "1993-06-21",
        "adresse_numero": "42",
        "adresse_rue": "Rue aléatoire",
        "adresse_ville": "Rennes",
        "adresse_code_postal": "35000",
        "telephone": "0612345678",
        "age_minimum": "",
    }


@pytest.mark.parametrize(
    "parametres, erreur, message_erreur",
    [
        ({"nom": 12}, TypeError, "Le nom doit être une instance de str."),
        ({"prenom": [1]}, TypeError, "Le prénom doit être une instance de str."),
        (
            {"date_naissance": "1993-06-21"},
            TypeError,
            "La date de naissance doit être une instance de datetime.date.",
        ),
        (
            {"adresse_numero": "12"},
            TypeError,
            "Le numéro de l'adresse postale doit être une instance de int.",
        ),
        (
            {"adresse_rue": {"Magnifique rue"}},
            TypeError,
            "La rue de l'adresse postale doit être une instance de str.",
        ),
        (
            {"adresse_ville": 12},
            TypeError,
            "La ville de l'adresse postale doit être une instance de str.",
        ),
        (
            {"adresse_code_postal": 35_000},
            TypeError,
            "Le code postal doit être une instance de str.",
        ),
        (
            {"adresse_code_postal": "35k"},
            ValueError,
            ("Le code postal doit être de longueur 5 et ne contenir que des " "chiffres."),
        ),
        (
            {"adresse_code_postal": "123456"},
            ValueError,
            ("Le code postal doit être de longueur 5 et ne contenir que des " "chiffres."),
        ),
        (
            {"adresse_code_postal": "12E45"},
            ValueError,
            ("Le code postal doit être de longueur 5 et ne contenir que des " "chiffres."),
        ),
        (
            {"telephone": 1234567890},
            TypeError,
            "Le numéro de téléphone doit être une instance de str si fourni.",
        ),
        (
            {"telephone": "123456789"},
            ValueError,
            (
                "Si le numéro de téléphone est fourni, il doit être de "
                "longueur 10, commencer par 0 et ne contenir que des chiffres."
            ),
        ),
        (
            {"telephone": "1234567890"},
            ValueError,
            (
                "Si le numéro de téléphone est fourni, il doit être de "
                "longueur 10, commencer par 0 et ne contenir que des chiffres."
            ),
        ),
        (
            {"telephone": "O123456789"},
            ValueError,
            (
                "Si le numéro de téléphone est fourni, il doit être de "
                "longueur 10, commencer par 0 et ne contenir que des chiffres."
            ),
        ),
        (
            {"age_minimum": 12.0},
            TypeError,
            "L'âge minimum doit être une instance de int si fourni.",
        ),
        ({"age_minimum": -1}, ValueError, "L'âge minimum doit être positif si fourni."),
        ({"age_minimum": 42}, ValueError, "Vous êtes trop jeune pour vous inscrire."),
    ],
)
def test_erreur_valider_questionnaire(dico, parametres, erreur, message_erreur):
    """Teste que l'erreur est bien soulevée comme attendu."""
    dico.update(**parametres)
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        valider_questionnaire(**dico)


@pytest.mark.parametrize(
    "parametres, erreur, message_erreur",
    [
        (
            {"date_naissance": "19930621"},
            (TypeError, ValueError),
            "Format invalide pour 'date_naissance'.",
        ),
        (
            {"date_naissance": "1993-16-21"},
            (TypeError, ValueError),
            "Format invalide pour 'date_naissance'.",
        ),
        (
            {"date_naissance": "1993-06-32"},
            (TypeError, ValueError),
            "Format invalide pour 'date_naissance'.",
        ),
        (
            {"adresse_numero": "[12]"},
            (TypeError, ValueError),
            "Format invalide pour 'adresse_numero'.",
        ),
        (
            {"adresse_numero": "abc"},
            (TypeError, ValueError),
            "Format invalide pour 'adresse_numero'.",
        ),
        (
            {"adresse_code_postal": "O1234"},
            ValueError,
            "Le code postal doit être de longueur 5 et ne contenir que des " "chiffres.",
        ),
        (
            {"adresse_code_postal": "012345"},
            ValueError,
            "Le code postal doit être de longueur 5 et ne contenir que des " "chiffres.",
        ),
        (
            {"telephone": "1234567890"},
            ValueError,
            "Si 'telephone' est fourni, il doit être de longueur 10, "
            "commencer par 0 et ne contenir que des chiffres.",
        ),
        (
            {"telephone": "012345678"},
            ValueError,
            "Si 'telephone' est fourni, il doit être de longueur 10, "
            "commencer par 0 et ne contenir que des chiffres.",
        ),
        (
            {"telephone": "O123456789"},
            ValueError,
            "Si 'telephone' est fourni, il doit être de longueur 10, "
            "commencer par 0 et ne contenir que des chiffres.",
        ),
        (
            {"age_minimum": "dix-huit"},
            (TypeError, ValueError),
            "Format invalide pour 'age_minimum'.",
        ),
        (
            {"age_minimum": "[18]"},
            (TypeError, ValueError),
            "Format invalide pour 'age_minimum'.",
        ),
        (
            {"age_minimum": "-1"},
            ValueError,
            "'age_minimum' doit être positif si fourni.",
        ),
        ({"age_minimum": "42"}, ValueError, "Vous êtes trop jeune pour vous inscrire."),
    ],
)
def test_erreur_valider_questionnaire_str(dico_str, parametres, erreur, message_erreur):
    """Teste que l'erreur est bien soulevée comme attendu."""
    dico_str.update(**parametres)
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        valider_questionnaire_str(**dico_str)


@pytest.mark.parametrize(
    "parametres, parametres_str",
    [
        ({}, {}),
        (
            {"date_naissance": datetime.date(1995, 12, 31)},
            {"date_naissance": "1995-12-31"},
        ),
        ({"adresse_numero": 365}, {"adresse_numero": "365"}),
        ({"telephone": None}, {"telephone": ""}),
        ({"age_minimum": 21}, {"age_minimum": "21"}),
    ],
)
def test_sortie_valider_questionnaire_str(dico, dico_str, parametres, parametres_str):
    """Teste que la sortie renvoyée correspond bien à la sortie attendue."""
    dico.update(**parametres)
    dico_str.update(**parametres_str)
    assert valider_questionnaire_str(**dico_str) == dico
