class Entreprise:
    """Entreprise.

    Parameters
    ----------
    nom : str
        Nom de l'entreprise.

    commune : str
        Commune où l'entreprise est implémentée.

    chiffre_affaire : int
        Chiffre d'affaire annuel.

    """

    def __init__(self, nom: str, commune: str, chiffre_affaires: int):
        self.nom = nom
        self.commune = commune
        self.chiffre_affaires = chiffre_affaires
        self.__nombre_demissions: int = 0
        self.__nombre_licenciements: int = 0
        self.__nombre_ruptures_amiable: int = 0

    @property
    def nombre_demissions(self) -> int:
        return self.__nombre_demissions

    @property
    def nombre_nombre_licenciements(self) -> int:
        return self.__nombre_licenciements

    @property
    def nombre_ruptures_amiable(self) -> int:
        return self.__nombre_ruptures_amiable

    def incrementer_nombre_demissions(self) -> None:
        """Incrémente le nombre de démissions d'une unité."""
        self.__nombre_demissions += 1

    def incrementer_nombre_licenciements(self) -> None:
        """Incrémente le nombre de licenciements d'une unité."""
        self.__nombre_licenciements += 1

    def incrementer_nombre_ruptures_amiable(self) -> None:
        """Incrémente le nombre de ruptures à l'amiable d'une unité."""
        self.__nombre_ruptures_amiable += 1
