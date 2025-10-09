"""Fonctions de validation d'une inscription."""


def valider_adresse_electronique(adresse_electronique: str) -> None:
    """Valide une adresse électronique.

    Une adresse électronique est composée des trois éléments suivants, dans
    cet ordre :
        - Une partie locale (ou préfixe)
        - Le séparateur, qui est le symbole @
        - L'adresse du serveur, qui est une liste de labels séparés par des
          signes point

    Une adresse électronique est valide si et seulement si :
        - Elle contient un seul symbole @.
        - Le signe point ne peut se trouver au début, à la fin ou être répété
          (c-à-d deux fois à la suite) ni dans la partie locale, ni dans
          l'adresse du serveur.
        - La partie locale contient entre 1 et 64 caractères.
        - L'adresse du serveur est non-vide.
        - Chaque label de l'adresse du serveur contient au plus 63 caractères.

    Si au moins un critère n'est pas vérifié, alors une erreur doit être levée
    avec un message d'erreur explicite.

    Parameters
    ----------
    adresse_electronique : str
        Adresse electronique.

    Notes
    -----
    Ces règles ne sont pas tout à fait exactes et ont été simplifiées. Pour les
    personnes intéressées, vous pouvez regarder l'entrée Wikipedia de
    "Adresse électronique" :
    https://fr.wikipedia.org/wiki/Adresse_électronique.

    """

    def valider_signe_point(string: str, nom: str) -> None:
        if len(string) == 0:
            raise ValueError(f"{nom} ne peut pas être vide.")
        if string[0] == ".":
            raise ValueError(f"{nom} ne peut pas commencer par un signe point.")
        if string[-1] == ".":
            raise ValueError(f"{nom} ne peut pas se terminer par un signe point.")
        if ".." in string:
            raise ValueError(f"{nom} ne peut pas contenir deux signes point répétés.")

    nombre_at: int = adresse_electronique.count("@")
    if nombre_at != 1:
        raise ValueError("L'adresse électronique doit contenir un seul symbole @.")

    prefixe: str
    domaine: str
    prefixe, domaine = adresse_electronique.split("@")

    valider_signe_point(prefixe, "La partie locale")
    valider_signe_point(domaine, "L'adresse du serveur")

    if not (1 <= len(prefixe) <= 64):
        raise ValueError("La partie locale doit contenir entre 1 et 64 caractères inclus.")

    if any(len(sub) > 63 for sub in domaine.split(".")):
        raise ValueError("Les labels de l'adresse du serveur doivent contenir au plus 63 caractères.")


def valider_mot_de_passe(mot_de_passe: str) -> None:
    """Valide un mot de passe.

    Un mot de passe est valide si et seulement si :
        - Il contient entre 12 et 256 caractères
        - Il contient au moins :
            * une majuscule,
            * une minuscule,
            * un chiffre, et
            * un caractère spécial (~ @ # _ ^ * € % / . + : ; =)

    Si au moins un critère n'est pas vérifié, alors une erreur doit être levée
    avec un message explicite.

    Parameters
    ----------
    mot_de_passe : str
        Mot de passe

    """
    if not (12 <= len(mot_de_passe) <= 256):
        raise ValueError("Le mot de passe doit contenir entre 12 et 256 caractères.")

    if not any(char.isupper() for char in mot_de_passe):
        raise ValueError("Le mot de passe doit contenir au moins une majuscule.")

    if not any(char.islower() for char in mot_de_passe):
        raise ValueError("Le mot de passe doit contenir au moins une minuscule.")

    if not any(char.isdigit() for char in mot_de_passe):
        raise ValueError("Le mot de passe doit contenir au moins un chiffre.")

    caracteres_speciaux = "~@#_^*€%/.+:;="
    if not any(char in caracteres_speciaux for char in mot_de_passe):
        raise ValueError("Le mot de passe doit contenir au moins un caractère spécial.")


def valider_second_mot_de_passe(mot_de_passe_1: str, mot_de_passe_2: str) -> None:
    """Valide le deuxième mot de passe.

    Les deux mots de passe doivent être égaux. Si ce n'est pas le cas, une erreur est
    levée.

    Parameters
    ----------
    mot_de_passe_1, mot_de_passe_2 : str
        Mots de passe entrés.
    """
    if not (mot_de_passe_1 == mot_de_passe_2):
        raise ValueError("Les deux mots de passe ne correspondent pas.")
