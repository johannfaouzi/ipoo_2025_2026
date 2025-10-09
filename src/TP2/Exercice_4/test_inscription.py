import re

import pytest

from .inscription import (
    valider_adresse_electronique,
    valider_mot_de_passe,
    valider_second_mot_de_passe,
)

caracteres_speciaux = "~@#_^*€%/.+:;="


@pytest.mark.parametrize(
    "adresse_electronique, valide, message_erreur",
    [
        ("johann.faouzi@ensai.fr", True, None),
        ("prenom.nom@ensai.fr", True, None),
        ("prenom.nom@eleve.ensai.fr", True, None),
        ("prenom.nom@eleve.1A.ensai.fr", True, None),
        (
            "johann.faouzi@ensai@fr",
            False,
            "L'adresse électronique doit contenir un seul symbole @.",
        ),
        ("@johann.faouzi.ensai.fr", False, "La partie locale ne peut pas être vide."),
        (
            ".johann.faouzi@.ensai.fr",
            False,
            "La partie locale ne peut pas commencer par un signe point.",
        ),
        (
            "johann.faouzi.@ensai.fr",
            False,
            "La partie locale ne peut pas se terminer par un signe point.",
        ),
        (
            "johann..faouzi@ensai.fr",
            False,
            "La partie locale ne peut pas contenir deux signes point répétés.",
        ),
        ("johann.faouzi@", False, "L'adresse du serveur ne peut pas être vide."),
        (
            "johann.faouzi@.ensai.fr",
            False,
            "L'adresse du serveur ne peut pas commencer par un signe point.",
        ),
        (
            "johann.faouzi@ensai.fr.",
            False,
            "L'adresse du serveur ne peut pas se terminer par un signe point.",
        ),
        (
            "johann.faouzi@ensai..fr",
            False,
            "L'adresse du serveur ne peut pas contenir deux signes point " "répétés.",
        ),
        (
            f"{'j' * 65}@ensai.fr",
            False,
            "La partie locale doit contenir entre 1 et 64 caractères inclus.",
        ),
        (
            f"johann.faouzi@ensai.{'a' * 64}.fr",
            False,
            "Les labels de l'adresse du serveur doivent contenir " "au plus 63 caractères.",
        ),
    ],
)
def test_valider_adresse_electronique(
    adresse_electronique: str,
    valide: bool,
    message_erreur: str,
):
    """Tests pour la fonction valider_adresse_electronique."""
    if valide:
        valider_adresse_electronique(adresse_electronique)
    else:
        with pytest.raises(ValueError, match=re.escape(message_erreur)):
            valider_adresse_electronique(adresse_electronique)


@pytest.mark.parametrize(
    "mot_de_passe, message_erreur",
    [
        ("P@$$w0rd1234", None),
        *[(f"Passw0rd1234{char}", None) for char in caracteres_speciaux],
        ("p4ssWord_abcd;", None),
        ("a" * 11, "Le mot de passe doit contenir entre 12 et 256 caractères."),
        ("a" * 257, "Le mot de passe doit contenir entre 12 et 256 caractères."),
        ("a" * 24, "Le mot de passe doit contenir au moins une majuscule."),
        ("A" * 24, "Le mot de passe doit contenir au moins une minuscule."),
        ("Aa" * 12, "Le mot de passe doit contenir au moins un chiffre."),
        ("Aa1" * 4, "Le mot de passe doit contenir au moins un caractère spécial."),
    ],
)
def test_valider_mot_de_passe(mot_de_passe: str, message_erreur: str | None):
    """Tests pour la fonction valider_mot_de_passe."""
    if message_erreur is None:
        valider_mot_de_passe(mot_de_passe)
    else:
        with pytest.raises(ValueError, match=re.escape(message_erreur)):
            valider_mot_de_passe(mot_de_passe)


@pytest.mark.parametrize(
    "mot_de_passe_1, mot_de_passe_2, valide",
    [
        ("P@$$w0rd", "P@$$w0rd", True),
        ("P@$$w0rd", "P@$$word", False),
        ("P4$$w0rd", "P@$$w0rd", False),
        ("p@$$w0rd", "P@$$w0rd", False),
        ("password", "P@$$w0rd", False),
    ],
)
def test_valider_second_mot_de_passe(
    mot_de_passe_1: str,
    mot_de_passe_2: str,
    valide: bool,
):
    """Tests pour la fonction valider_second_mot_de_passe."""
    if valide:
        valider_second_mot_de_passe(mot_de_passe_1, mot_de_passe_2)
    else:
        with pytest.raises(ValueError, match=re.escape("Les deux mots de passe ne correspondent pas.")):
            valider_second_mot_de_passe(mot_de_passe_1, mot_de_passe_2)
