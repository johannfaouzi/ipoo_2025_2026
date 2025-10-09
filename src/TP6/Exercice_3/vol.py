import datetime
import warnings

from .aeroport import Aeroport
from .compagnie import Compagnie


class Vol:
    """Classe modélisant un vol.

    Parameters
    ----------
    id : int
        Identifiant unique du vol.

    numero : int
        Numéro du vol.

    compagnie : Compagnie
        Compagnie aérienne assurant le vol.

    aeroport_depart : Aeroport
        Aéroport au départ.

    aeroport_arrivee : Aeroport
        Aéroport à l'arrivée.

    horaire_depart : datetime.datetime
        Horaire de départ du vol.

    horaire_arrivee : datetime.datetime
        Horaire d'arrivée du vol.
    """

    def __init__(
        self,
        id: int,
        numero: int,
        compagnie: Compagnie,
        aeroport_depart: Aeroport,
        aeroport_arrivee: Aeroport,
        horaire_depart: datetime.datetime,
        horaire_arrivee: datetime.datetime,
    ):
        if not isinstance(id, int):
            raise TypeError("L'identifiant doit être un entier.")
        if not isinstance(compagnie, Compagnie):
            raise TypeError("La compagnie aérienne doit être une instance de Compagnie.")
        if not isinstance(numero, int):
            raise TypeError("Le numéro doit être un entier.")
        if not isinstance(aeroport_depart, Aeroport):
            raise TypeError("L'aéroport de départ doit être une instance de Aeroport.")
        if not isinstance(aeroport_arrivee, Aeroport):
            raise TypeError("L'aéroport d'arrivée doit être une instance de Aeroport.")
        if not isinstance(horaire_depart, datetime.datetime):
            raise TypeError("L'horaire de départ doit être une instance de " "datetime.datetime.")
        if not isinstance(horaire_arrivee, datetime.datetime):
            raise TypeError("L'horaire d'arrivée doit être une instance de " "datetime.datetime.")

        if (horaire_depart.hour == 0) and (horaire_depart.minute == 0):
            warnings.warn(
                "L'heure de départ est minuit, ce qui est la valeur par "
                "défaut. Vérifiez qu'il s'agit bien de l'heure de départ de "
                "votre vol.",
                UserWarning,
            )
        if (horaire_arrivee.hour == 0) and (horaire_arrivee.minute == 0):
            warnings.warn(
                "L'heure d'arrivée est minuit, ce qui est la valeur par "
                "défaut. Vérifiez qu'il s'agit bien de l'heure d'arrivée de "
                "votre vol.",
                UserWarning,
            )

        self._id = id
        self.compagnie = compagnie
        self.numero = numero
        self.aeroport_depart = aeroport_depart
        self.aeroport_arrivee = aeroport_arrivee
        self.horaire_depart = horaire_depart
        self.horaire_arrivee = horaire_arrivee
        self._reservation_ouverte: bool = False

    def _ouvrir_reservation(self) -> None:
        """Ouvre la réservation de ce vol."""
        if self._reservation_ouverte:
            raise ValueError("La réservation est déjà ouverte.")
        self._reservation_ouverte = True

    def _fermer_reservation(self) -> None:
        """Ferme la réservation de ce vol."""
        if not self._reservation_ouverte:
            raise ValueError("La réservation est déjà fermée.")
        self._reservation_ouverte = False
