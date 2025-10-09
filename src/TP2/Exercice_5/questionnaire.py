"""Fonctions de validation d'un questionnaire."""

import datetime


def valider_questionnaire(
    nom: str,
    prenom: str,
    date_naissance: datetime.date,
    adresse_numero: int,
    adresse_rue: str,
    adresse_ville: str,
    adresse_code_postal: str,
    telephone: str | None = None,
    age_minimum: int | None = None,
) -> None:
    """Valide les  dentrées du questionnaire.

    Parameters
    ----------
    nom : str
        Nom.

    prenom : str
        Prénom.

    date_naissance : datetime.date
        Date de naissance.

    adresse_numero : int
        Numéro de l'adresse postale.

    adresse_rue : str
        Nom de la rue de l'adresse postale.

    adresse_ville : str
        Ville de l'adresse postale.

    adresse_code_postal : str
        Code postal de la ville, composé de 5 chiffres.

    telephone : None or str (default = None)
        Numéro de téléphone.

    age_minimum : None or int (default = None)
        Age minimum (uniquement pris en compte si fourni)

    """

    if not isinstance(nom, str):
        raise TypeError("Le nom doit être une instance de str.")

    if not isinstance(prenom, str):
        raise TypeError("Le prénom doit être une instance de str.")

    if not isinstance(date_naissance, datetime.date):
        raise TypeError("La date de naissance doit être une instance de datetime.date.")

    if not isinstance(adresse_numero, int):
        raise TypeError("Le numéro de l'adresse postale doit être une instance de int.")

    if not isinstance(adresse_rue, str):
        raise TypeError("La rue de l'adresse postale doit être une instance de str.")

    if not isinstance(adresse_ville, str):
        raise TypeError("La ville de l'adresse postale doit être une instance de str.")

    if not isinstance(adresse_code_postal, str):
        raise TypeError("Le code postal doit être une instance de str.")
    if isinstance(adresse_code_postal, str):
        if (len(adresse_code_postal) != 5) or (not adresse_code_postal.isdigit()):
            raise ValueError("Le code postal doit être de longueur 5 et " "ne contenir que des chiffres.")

    if not ((telephone is None) or isinstance(telephone, str)):
        raise TypeError("Le numéro de téléphone doit être une instance de str si fourni.")
    if isinstance(telephone, str):
        if (len(telephone) != 10) or (not telephone.isdigit()) or (telephone[0] != "0"):
            raise ValueError(
                "Si le numéro de téléphone est fourni, il doit être de "
                "longueur 10, commencer par 0 et ne contenir que des chiffres."
            )

    if not ((age_minimum is None) or isinstance(age_minimum, int)):
        raise TypeError("L'âge minimum doit être une instance de int si fourni.")
    if isinstance(age_minimum, int):
        if age_minimum < 0:
            raise ValueError("L'âge minimum doit être positif si fourni.")
        today = date_naissance.today()

        age = today.year - date_naissance.year
        if date_naissance.month > today.month:
            age -= 1
        else:
            if date_naissance.day > today.day:
                age -= 1

        if age < age_minimum:
            raise ValueError("Vous êtes trop jeune pour vous inscrire.")


def valider_questionnaire_str(
    nom: str,
    prenom: str,
    date_naissance: str,
    adresse_numero: str,
    adresse_rue: str,
    adresse_ville: str,
    adresse_code_postal: str,
    telephone: str = "",
    age_minimum: str = "",
) -> dict[str, str | datetime.date | int | None]:
    """Valide les  dentrées du questionnaire.

    Parameters
    ----------
    nom : str
        Nom.

    prenom : str
        Prénom.

    date_naissance : str
        Date de naissance au format AAAA-MM-JJ.

    adresse_numero : str
        Numéro de l'adresse postale.

    adresse_rue : str
        Nom de la rue de l'adresse postale.

    adresse_ville : str
        Ville de l'adresse postale.

    adresse_code_postal : str
        Code postal de la ville, composé de 5 chiffres.

    telephone : str (default = '')
        Numéro de téléphone.

    age_minimum : str (default = '')
        Age minimum (uniquement pris en compte si fourni)

    Returns
    -------
    dict
        Dictionnaire avec les entrées validées (et éventuellement transformées)

    """
    try:
        year_str: str
        month_str: str
        day_str: str
        year_str, month_str, day_str = date_naissance.split("-")
        year: int = int(year_str)
        month: int = int(month_str)
        day: int = int(day_str)
        date_naissance_datetime = datetime.date(year, month, day)
    except (TypeError, ValueError):
        raise ValueError("Format invalide pour 'date_naissance'.")

    try:
        adresse_numero_int: int = int(adresse_numero)
    except (TypeError, ValueError):
        raise ValueError("Format invalide pour 'adresse_numero'.")

    if (len(adresse_code_postal) != 5) or (not adresse_code_postal.isdigit()):
        raise ValueError("Le code postal doit être de longueur 5 et " "ne contenir que des chiffres.")

    telephone_res: str | None
    if len(telephone):
        if (len(telephone) != 10) or (not telephone.isdigit()) or (telephone[0] != "0"):
            raise ValueError(
                "Si 'telephone' est fourni, il doit être de longueur 10, "
                "commencer par 0 et ne contenir que des chiffres."
            )
        telephone_res = telephone
    else:
        telephone_res = None

    age_minimum_res: int | None
    if len(age_minimum):
        try:
            age_minimum_res = int(age_minimum)
        except (TypeError, ValueError):
            raise ValueError("Format invalide pour 'age_minimum'.")

        if age_minimum_res < 0:
            raise ValueError("'age_minimum' doit être positif si fourni.")
        today: datetime.date = date_naissance_datetime.today()

        age: int = today.year - date_naissance_datetime.year
        if date_naissance_datetime.month > today.month:
            age -= 1
        else:
            if date_naissance_datetime.day > today.day:
                age -= 1

        if age < age_minimum_res:
            raise ValueError("Vous êtes trop jeune pour vous inscrire.")
    else:
        age_minimum_res = None

    res: dict[str, str | datetime.date | int | None] = {
        "nom": nom,
        "prenom": prenom,
        "date_naissance": date_naissance_datetime,
        "adresse_numero": adresse_numero_int,
        "adresse_rue": adresse_rue,
        "adresse_ville": adresse_ville,
        "adresse_code_postal": adresse_code_postal,
        "telephone": telephone_res,
        "age_minimum": age_minimum_res,
    }

    return res
