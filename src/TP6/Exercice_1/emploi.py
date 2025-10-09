import datetime

from .entreprise import Entreprise
from .personne import Personne


class Emploi:
    """Emploi.

    Parameters
    ----------
    employe : Personne
        Employé.

    entreprise : Entreprise.
        Employeur.

    type_contrat : {'CDD', 'CDI'}
        Type de contrat de travail.

    date_debut : datetime.date
        Date du début du contrat de travail.

    date_fin : datetime.date or None (default = None)
        Date de fin du contrat de travail.
    """

    def __init__(
        self,
        employe: Personne,
        entreprise: Entreprise,
        type_contrat: str,
        date_debut: datetime.date,
        date_fin: datetime.date | None = None,
    ) -> None:
        self.employe = employe
        self.entreprise = entreprise
        self.type_contrat = type_contrat
        self.date_debut = date_debut
        self.date_fin = date_fin

    def prolonger_contrat(self, nouvelle_date_fin: datetime.date) -> None:
        """Prolongation du contrat de travail.

        Parameters
        ----------
        nouvelle_date_fin : datetime.date
            Nouvelle date de fin du contrat
        """
        if not (isinstance(self.date_fin, datetime.date) and nouvelle_date_fin > self.date_fin):
            raise ValueError("'La nouvelle date de fin doit être " "postérieure à la date de fin actuelle.")
        self.date_fin = nouvelle_date_fin

    def rupture_contrat(self, nouvelle_date_fin: datetime.date, motif: str) -> None:
        """Rupture du contrat avant la date de fin prévue.

        Parameters
        ----------
        nouvelle_date_fin : datetime.date
            Date de la nouvelle fin du contrat

        motif : {'démission', 'licenciement', "accord à l'amiable"}
            Motif de la rupture du contrat.
        """
        if motif == "démission":
            self.employe.mise_a_jour_demission()
            self.entreprise.incrementer_nombre_demissions()
        elif motif == "licenciement":
            self.employe.mise_a_jour_licenciement()
            self.entreprise.incrementer_nombre_licenciements()
        elif motif == "accord à l'amiable":
            self.employe.mise_a_jour_rupture_amiable()
            self.entreprise.incrementer_nombre_ruptures_amiable()
        else:
            raise ValueError("'motif' non valide.")

        self.date_fin = nouvelle_date_fin

        self.employe.experience_professionnelle += (
            f"{'\n' if len(self.employe.experience_professionnelle) > 0 else ''}"
            f"* Emploi en {self.type_contrat} chez {self.entreprise.nom} du {self.date_debut} au {nouvelle_date_fin}."
        )

    def __str__(self) -> str:
        """Conversion en chaîne de caractères."""
        fin: str
        if self.date_fin is not None:
            fin = f" et se terminant le {self.date_fin}"
        else:
            fin = ""
        string: str = (
            f"L'entreprise {repr(self.entreprise.nom)} "
            f"emploie {self.employe.prenom} {self.employe.nom} "
            f"sur un contrat à durée "
            f"{'in' if self.type_contrat == 'CDI' else ''}déterminé "
            f"ayant débuté le {self.date_debut}{fin}."
        )
        return string
