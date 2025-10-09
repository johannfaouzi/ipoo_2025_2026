import re
from datetime import datetime

import pytest

from ..compagnie import Compagnie
from ..vol import Vol


@pytest.mark.parametrize(
    "kwargs, message_erreur",
    [
        ({"id": "123"}, "L'identifiant doit être un entier."),
        ({"id": [123]}, "L'identifiant doit être un entier."),
        (
            {"compagnie": "Air France-KLM"},
            ("La compagnie aérienne doit être une instance de Compagnie."),
        ),
        (
            {"compagnie": ["Air France-KLM"]},
            ("La compagnie aérienne doit être une instance de Compagnie."),
        ),
        ({"numero": "456"}, "Le numéro doit être un entier."),
        ({"numero": {456}}, "Le numéro doit être un entier."),
        (
            {"aeroport_depart": "Aéroport Rennes Bretagne"},
            ("L'aéroport de départ doit être une instance de Aeroport."),
        ),
        (
            {"aeroport_depart": Compagnie("Air France-KLM")},
            ("L'aéroport de départ doit être une instance de Aeroport."),
        ),
        (
            {"aeroport_arrivee": "Aéroport Rennes Bretagne"},
            ("L'aéroport d'arrivée doit être une instance de Aeroport."),
        ),
        (
            {"aeroport_arrivee": Compagnie("Aéroport Nice-Côte d'Azur")},
            ("L'aéroport d'arrivée doit être une instance de Aeroport."),
        ),
        (
            {"horaire_depart": "2024/12/3 14:45"},
            ("L'horaire de départ doit être une instance de datetime.datetime."),
        ),
        (
            {"horaire_depart": [datetime(2024, 4, 29, 15, 10)]},
            ("L'horaire de départ doit être une instance de datetime.datetime."),
        ),
        (
            {"horaire_arrivee": "2024/12/3 14:45"},
            ("L'horaire d'arrivée doit être une instance de datetime.datetime."),
        ),
        (
            {"horaire_arrivee": {datetime(2024, 4, 29, 15, 10)}},
            ("L'horaire d'arrivée doit être une instance de datetime.datetime."),
        ),
    ],
)
def test_vol_init_erreur(vol_kwargs, kwargs, message_erreur):
    vol_kwargs.update(**kwargs)
    with pytest.raises(TypeError, match=re.escape(message_erreur)):
        Vol(**vol_kwargs)


@pytest.mark.parametrize(
    "kwargs, message",
    [
        (
            {"horaire_depart": datetime(2024, 4, 29)},
            (
                "L'heure de départ est minuit, ce qui est la valeur par défaut. "
                "Vérifiez qu'il s'agit bien de l'heure de départ de votre vol."
            ),
        ),
        (
            {"horaire_depart": datetime(2024, 4, 29, hour=0)},
            (
                "L'heure de départ est minuit, ce qui est la valeur par défaut. "
                "Vérifiez qu'il s'agit bien de l'heure de départ de votre vol."
            ),
        ),
        (
            {"horaire_depart": datetime(2024, 4, 29, minute=0)},
            (
                "L'heure de départ est minuit, ce qui est la valeur par défaut. "
                "Vérifiez qu'il s'agit bien de l'heure de départ de votre vol."
            ),
        ),
        (
            {"horaire_depart": datetime(2024, 4, 29, 0, 0)},
            (
                "L'heure de départ est minuit, ce qui est la valeur par défaut. "
                "Vérifiez qu'il s'agit bien de l'heure de départ de votre vol."
            ),
        ),
        (
            {"horaire_arrivee": datetime(2024, 4, 30)},
            (
                "L'heure d'arrivée est minuit, ce qui est la valeur par défaut. "
                "Vérifiez qu'il s'agit bien de l'heure d'arrivée de votre vol."
            ),
        ),
        (
            {"horaire_arrivee": datetime(2024, 4, 30, hour=0)},
            (
                "L'heure d'arrivée est minuit, ce qui est la valeur par défaut. "
                "Vérifiez qu'il s'agit bien de l'heure d'arrivée de votre vol."
            ),
        ),
        (
            {"horaire_arrivee": datetime(2024, 4, 30, minute=0)},
            (
                "L'heure d'arrivée est minuit, ce qui est la valeur par défaut. "
                "Vérifiez qu'il s'agit bien de l'heure d'arrivée de votre vol."
            ),
        ),
        (
            {"horaire_arrivee": datetime(2024, 4, 30, 0, 0)},
            (
                "L'heure d'arrivée est minuit, ce qui est la valeur par défaut. "
                "Vérifiez qu'il s'agit bien de l'heure d'arrivée de votre vol."
            ),
        ),
    ],
)
def test_vol_init_avertissement(vol_kwargs, kwargs, message):
    vol_kwargs.update(**kwargs)
    with pytest.warns(UserWarning, match=re.escape(message)):
        Vol(**vol_kwargs)


@pytest.mark.parametrize("parametres", [{"_reservation_ouverte": True}, ("_ouvrir_reservation",)])
def test_vol_ouvrir_reservation_erreur(vol_kwargs, parametres):
    vol = Vol(**vol_kwargs)
    if isinstance(parametres, dict):
        setattr(vol, "_reservation_ouverte", parametres["_reservation_ouverte"])
    else:
        pass
        for method in parametres:
            getattr(vol, method)()
    with pytest.raises(ValueError, match=re.escape("La réservation est déjà ouverte.")):
        vol._ouvrir_reservation()


@pytest.mark.parametrize("parametres", [{"_reservation_ouverte": False}, {}])
def test_vol_fermer_reservation_erreur(vol_kwargs, parametres):
    vol = Vol(**vol_kwargs)
    if "_reservation_ouverte" in parametres.keys():
        setattr(vol, "_reservation_ouverte", parametres["_reservation_ouverte"])
    with pytest.raises(ValueError, match=re.escape("La réservation est déjà fermée.")):
        vol._fermer_reservation()


@pytest.mark.parametrize(
    "actions, resultat_attendu",
    [
        (("_ouvrir_reservation",), True),
        (("_ouvrir_reservation", "_fermer_reservation"), False),
        (("_ouvrir_reservation", "_fermer_reservation", "_ouvrir_reservation"), True),
        (
            (
                "_ouvrir_reservation",
                "_fermer_reservation",
                "_ouvrir_reservation",
                "_fermer_reservation",
            ),
            False,
        ),
    ],
)
def test_vol_ouvrir_fermer_reservation(vol_kwargs, actions, resultat_attendu):
    vol = Vol(**vol_kwargs)
    for method in actions:
        getattr(vol, method)()
    assert vol._reservation_ouverte is resultat_attendu
