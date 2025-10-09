class Aeroport:
    """Classe modélisant un aéroport.

    Parameters
    ----------
    nom : str
        Nom de l'aéroport.

    ville : str
        Ville associée à l'aéroport.
    """

    def __init__(self, nom: str, ville: str) -> None:
        if not isinstance(nom, str):
            raise TypeError("Le nom doit être une chaîne de caractères.")
        if not isinstance(ville, str):
            raise TypeError("La ville doit être une chaîne de caractères.")

        self.nom = nom
        self.ville = ville
