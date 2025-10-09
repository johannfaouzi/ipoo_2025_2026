class Personne:
    """Personne.

    Parameters
    ----------
    nom : str
        Nom de la personne.

    prenom : str
        Prénom de la personne.

    age : int
        Âge de la personne.

    education : str
        Chaîne de caractères décrivant le parcours scolaire.

    experience_professionnelle : str
        Chaîne de caractères décrivant l'expérience profesionnelle.
    """

    def __init__(self, nom: str, prenom: str, age: int, education: str, experience_professionnelle: str) -> None:
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.education = education
        self.experience_professionnelle = experience_professionnelle
        self.__demission: bool = False
        self.__licenciement: bool = False
        self.__rupture_amiable: bool = False

    @property
    def demission(self) -> bool:
        return self.__demission

    @property
    def licenciement(self) -> bool:
        return self.__licenciement

    @property
    def rupture_amiable(self) -> bool:
        return self.__rupture_amiable

    def mise_a_jour_demission(self) -> None:
        """Met l'attribut privé demission à True."""
        self.__demission = True

    def mise_a_jour_licenciement(self) -> None:
        """Met l'attribut privé licenciement à True."""
        self.__licenciement = True

    def mise_a_jour_rupture_amiable(self) -> None:
        """Met l'attribut privé rupture_amiable à True."""
        self.__rupture_amiable = True
