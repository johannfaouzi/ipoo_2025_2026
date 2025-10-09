import re

import pytest

from ..client import Client
from ..passager import Passager
from ..reservation import Reservation


@pytest.mark.parametrize(
    "kwargs, message_erreur",
    [
        ({"id": "13579"}, "L'identifiant doit être un entier."),
        ({"id": {13579}}, "L'identifiant doit être un entier."),
        ({"vol": "13579"}, "Le vol doit être une instance de Vol."),
        ({"vol": ["vol"]}, "Le vol doit être une instance de Vol."),
        ({"passager": "Nom prénom"}, "Le passager doit être une instance de Passager."),
        (
            {"passager": ["Nom prénom"]},
            "Le passager doit être une instance de Passager.",
        ),
        ({"client": "Nom prénom"}, "Le client doit être une instance de Client."),
        ({"client": {"Nom prénom"}}, "Le client doit être une instance de Client."),
    ],
)
def test_reservation_init(reservation_kwargs, kwargs, message_erreur):
    reservation_kwargs.update(**kwargs)
    with pytest.raises(TypeError, match=re.escape(message_erreur)):
        Reservation(**reservation_kwargs)


@pytest.mark.parametrize(
    "kwargs, actions, resultat_attendu",
    [
        (
            {},
            (),
            (
                "Le•la client•e Johann Faouzi a effectué une réservation pour "
                "le•la passager•ère Ikko Yamane pour aller de Rennes à Nice. "
                "Le vol concerné est le vol numéro 8412, assurée par la compagnie "
                "Air France-KLM, au départ de l'aéroport Rennes Bretagne le "
                "08/04/2024 à 15:10 et à destination de l'aéroport Nice-Côte "
                "d'Azur, avec une arrivée prévue le 08/04/2024 à 16:45. "
                "La réservation n'est pas encore confirmée."
            ),
        ),
        (
            {"client": Client("Ikko Yamane")},
            ("confirmer",),
            (
                "Le•la client•e Ikko Yamane a effectué une réservation pour "
                "le•la passager•ère Ikko Yamane pour aller de Rennes à Nice. "
                "Le vol concerné est le vol numéro 8412, assurée par la compagnie "
                "Air France-KLM, au départ de l'aéroport Rennes Bretagne le "
                "08/04/2024 à 15:10 et à destination de l'aéroport Nice-Côte "
                "d'Azur, avec une arrivée prévue le 08/04/2024 à 16:45. "
                "La réservation est confirmée."
            ),
        ),
        (
            {"passager": Passager("Cédric Herzet")},
            ("confirmer", "annuler"),
            (
                "Le•la client•e Johann Faouzi a effectué une réservation pour "
                "le•la passager•ère Cédric Herzet pour aller de Rennes à Nice. "
                "Le vol concerné est le vol numéro 8412, assurée par la compagnie "
                "Air France-KLM, au départ de l'aéroport Rennes Bretagne le "
                "08/04/2024 à 15:10 et à destination de l'aéroport Nice-Côte "
                "d'Azur, avec une arrivée prévue le 08/04/2024 à 16:45. "
                "La réservation a été annulée."
            ),
        ),
    ],
)
def test_reservation_str(reservation_kwargs, kwargs, actions, resultat_attendu):
    reservation_kwargs.update(kwargs)
    reservation = Reservation(**reservation_kwargs)
    reservation.vol._ouvrir_reservation()
    for method in actions:
        getattr(reservation, method)()
    assert str(reservation) == resultat_attendu


def test_reservation_annuler_erreur(reservation_kwargs):
    reservation = Reservation(**reservation_kwargs)
    with pytest.raises(
        ValueError,
        match=re.escape("La réservation n'est pas confirmée, vous ne " "pouvez donc pas l'annuler."),
    ):
        reservation.annuler()


def test_reservation_confirmer_erreur(reservation_kwargs):
    reservation = Reservation(**reservation_kwargs)
    with pytest.raises(ValueError, match=re.escape("Ce vol n'est pas encore réservable.")):
        reservation.confirmer()


@pytest.mark.parametrize(
    "actions, resultat_attendu",
    [
        (("confirmer",), True),
        (("confirmer", "annuler"), False),
        (("confirmer", "annuler", "confirmer"), True),
        (("confirmer", "annuler", "confirmer", "annuler"), False),
        (("confirmer", "annuler", "confirmer", "annuler", "confirmer"), True),
    ],
)
def test_reservation_annuler_confirmer(reservation_kwargs, actions, resultat_attendu):
    reservation = Reservation(**reservation_kwargs)
    reservation.vol._ouvrir_reservation()
    for method in actions:
        getattr(reservation, method)()
    assert reservation._Reservation__confirmee is resultat_attendu
    if actions[-1] == "confirmer":
        assert reservation.id in reservation.passager.reservations
        assert reservation.id in reservation.client.reservations
    else:
        assert reservation.id not in reservation.passager.reservations
        assert reservation.id not in reservation.client.reservations
