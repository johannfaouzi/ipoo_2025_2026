class Client:
    """Classe modélisant un client.

    Parameters
    ----------
    nom : str
        Nom du passager.

    Attributes
    ----------
    reservations : set[int]
        Ensemble des identifiants des réservations effectuées par ce client.
    """

    def __init__(self, nom: str) -> None:
        if not isinstance(nom, str):
            raise TypeError("Le nom doit être une chaîne de caractères.")
        self.nom = nom
        self.reservations: set[int] = set()
