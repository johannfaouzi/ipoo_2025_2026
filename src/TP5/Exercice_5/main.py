from .attaque import Attaque
from .dict_attaques import DICT_ATTAQUES
from .dict_base_pokemon import DICT_BASE_POKEMON
from .pokemon import Pokemon

# Définition de l'instance du Pokémon Dracaufeu
dracaufeu_params = DICT_BASE_POKEMON["Dracaufeu"].copy()
dracaufeu_params.update(
    niveau=80,
    liste_attaques=[
        Attaque(**DICT_ATTAQUES["Grincement"]),  # type: ignore
        Attaque(**DICT_ATTAQUES["Lance-Flammes"]),  # type: ignore
        Attaque(**DICT_ATTAQUES["Cru-Ailes"]),  # type: ignore
        Attaque(**DICT_ATTAQUES["Déflagration"]),  # type: ignore
    ],
)
dracaufeu = Pokemon(**dracaufeu_params)  # type: ignore


# Définition de l'instance du Pokémon Tortank
tortank_params = DICT_BASE_POKEMON["Tortank"].copy()
tortank_params.update(
    niveau=80,
    liste_attaques=[
        Attaque(**DICT_ATTAQUES["Croco Larme"]),  # type: ignore
        Attaque(**DICT_ATTAQUES["Vibraqua"]),  # type: ignore
        Attaque(**DICT_ATTAQUES["Morsure"]),  # type: ignore
        Attaque(**DICT_ATTAQUES["Hydrocanon"]),  # type: ignore
    ],
)
tortank = Pokemon(**tortank_params)  # type: ignore


# Combat entre Dracaufeu et Tortank
dracaufeu.attaque("Grincement", tortank)
tortank.attaque("Croco Larme", dracaufeu)
dracaufeu.attaque("Cru-Ailes", tortank)
tortank.attaque("Morsure", dracaufeu)
dracaufeu.attaque("Lance-Flammes", tortank)
tortank.attaque("Hydrocanon", dracaufeu)

# Dracaufeu est K.O. S'il essaye d'attaquer, une erreur est soulevée (décommenter la ligne suivante) :
# dracaufeu.attaquer('Déflagration', tortank)

# Si un Pokémon essaye de l'attaquer, une erreur est également soulevée (décommenter la ligne suivante) :
# tortank.attaquer('Hydrocanon', dracaufeu)
