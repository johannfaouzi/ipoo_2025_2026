import re

import pytest

from .connexion import connexion

base_de_donnees = [
    ("johann.faouzi@ensai.fr", "Yoyo123456!"),
    ("johann.faouzi@gmail.com", "Yoyo123456?"),
    ("prenom.nom@eleve.ensai.fr", "Mot_de_p4sse"),
]

message_erreur = "Les informations entrées sont erronées."


@pytest.mark.parametrize(
    "adresse_electronique, mot_de_passe, present",
    [
        ("johann.faouzi@ensai.fr", "random_password", False),
        ("johann.faouzi@ensai.fr", "Yoyo123456!", True),
        ("johann.faouzi@ensai.fr", "Yoyo123456?", False),
        ("prenom.nom@eleve.ensai.fr", "Mot_de_p4sse", True),
        ("prenom.nom@eleve.ensai.fr", "random_access_memory", False),
    ],
)
def test_connexion(adresse_electronique: str, mot_de_passe: str, present: bool):
    """Tests pour la fonction connexion."""
    if present:
        connexion(adresse_electronique, mot_de_passe, base_de_donnees)
    else:
        with pytest.raises(ValueError, match=re.escape(message_erreur)):
            connexion(adresse_electronique, mot_de_passe, base_de_donnees)
