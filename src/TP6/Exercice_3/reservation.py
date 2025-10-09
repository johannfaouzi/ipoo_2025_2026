from .client import Client
from .passager import Passager
from .vol import Vol


class Reservation:
    """Classe modélisant une réservation.

    Parameters
    ----------
    id : int
        Identifiant unique de la réservation.

    vol : Vol
        Vol concernée par la réservation.

    passager : Passager
        Passager concernée par la réservation.

    client : Client
        Client effectuant la réservation.
    """

    def __init__(self, id: int, vol: Vol, passager: Passager, client: Client):
        if not isinstance(id, int):
            raise TypeError("L'identifiant doit être un entier.")
        if not isinstance(vol, Vol):
            raise TypeError("Le vol doit être une instance de Vol.")
        if not isinstance(passager, Passager):
            raise TypeError("Le passager doit être une instance de Passager.")
        if not isinstance(client, Client):
            raise TypeError("Le client doit être une instance de Client.")

        self.id = id
        self.vol = vol
        self.passager = passager
        self.client = client
        self.__confirmee: bool | None = None

    def __str__(self) -> str:
        if self.__confirmee is None:
            confirmee_annulee = "n'est pas encore confirmée"
        elif self.__confirmee is True:
            confirmee_annulee = "est confirmée"
        else:
            confirmee_annulee = "a été annulée"

        return (
            f"Le•la client•e {self.client.nom} a effectué une réservation "
            f"pour le•la passager•ère {self.passager.nom} pour aller de "
            f"{self.vol.aeroport_depart.ville} à "
            f"{self.vol.aeroport_arrivee.ville}. "
            f"Le vol concerné est le vol numéro {self.vol.numero}, assurée "
            f"par la compagnie {self.vol.compagnie.nom}, au départ "
            f"de l'aéroport {self.vol.aeroport_depart.nom} le "
            f"{self.vol.horaire_depart.day:02d}/"
            f"{self.vol.horaire_depart.month:02d}/"
            f"{self.vol.horaire_depart.year} à "
            f"{self.vol.horaire_depart.hour}:{self.vol.horaire_depart.minute} "
            f"et à destination de l'aéroport {self.vol.aeroport_arrivee.nom}, "
            f"avec une arrivée prévue le {self.vol.horaire_arrivee.day:02d}/"
            f"{self.vol.horaire_arrivee.month:02d}/"
            f"{self.vol.horaire_arrivee.year} "
            f"à {self.vol.horaire_arrivee.hour}:"
            f"{self.vol.horaire_arrivee.minute}. "
            f"La réservation {confirmee_annulee}."
        )

    def annuler(self) -> None:
        """Annule la réservation.

        La réservation ne peut être annulée que si elle a d'abord été
        confirmée. Si c'est bien le cas, la réservation est supprimée de
        l'ensemble des réservations du client et du passager.
        """
        if self.__confirmee is not True:
            raise ValueError("La réservation n'est pas confirmée, vous ne " "pouvez donc pas l'annuler.")
        self.__confirmee = False
        self.passager.reservations.remove(self.id)
        self.client.reservations.remove(self.id)

    def confirmer(self) -> None:
        """Confirme la réservation.

        La réservation ne peut être confirmée que si les réservations pour
        le vol sont bien ouvertes. Si c'est bien le cas, la réservation est
        ajoutée à l'ensembmble des réservations du client et du passager.
        """
        if not self.vol._reservation_ouverte:
            raise ValueError("Ce vol n'est pas encore réservable.")
        self.__confirmee = True
        self.passager.reservations.add(self.id)
        self.client.reservations.add(self.id)
