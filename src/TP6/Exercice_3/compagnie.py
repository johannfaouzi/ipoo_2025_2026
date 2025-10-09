class Compagnie:
    """Classe modélisant une compagnie aérienne.

    Parameters
    ----------
    nom : str
        Nom de la compagnie aérienne.
    """

    def __init__(self, nom: str) -> None:
        if not isinstance(nom, str):
            raise TypeError("Le nom doit être une chaîne de caractères.")
        self.nom = nom
