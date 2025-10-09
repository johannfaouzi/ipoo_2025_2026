from datetime import datetime

import pytest

from ..aeroport import Aeroport
from ..client import Client
from ..compagnie import Compagnie
from ..passager import Passager
from ..vol import Vol


@pytest.fixture
def vol_kwargs():
    return dict(
        id=1234,
        compagnie=Compagnie("Air France-KLM"),
        numero=8412,
        aeroport_depart=Aeroport("Rennes Bretagne", "Rennes"),
        aeroport_arrivee=Aeroport("Nice-Côte d'Azur", "Nice"),
        horaire_depart=datetime(2024, 4, 8, 15, 10),
        horaire_arrivee=datetime(2024, 4, 8, 16, 45),
    )


@pytest.fixture
def reservation_kwargs(vol_kwargs):
    return dict(
        id=456_789,
        vol=Vol(**vol_kwargs),
        passager=Passager("Ikko Yamane"),
        client=Client("Johann Faouzi"),
    )
