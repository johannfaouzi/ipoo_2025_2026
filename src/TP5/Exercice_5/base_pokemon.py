from .types import TYPES


class BasePokemon:
    """Classe de base d'un Pokémon.

    Cette classe contient toutes les informations générales sur un Pokémon.

    Parameters
    ----------
    id_ : int
        Identifiant du Pokémon (numéro dans le Pokédex). Doit être strictement positif.

    nom : str
        Nom du Pokémon.

    types : tuple[str] | tuple[str, str]
        Type(s) du Pokémon. Si le Pokémon n'a qu'un type, le tuple est de longeur 1, sinon de longueur 2.

    stat_pv : int
        Points de vie. Doit être strictement positif.

    stat_attaque : int
        Statistique d'attaque. Doit être strictement positif.

    stat_defense : int
        Statistique de défense. Doit être strictement positif.

    stat_attaque_speciale : int
        Statistique d'attaque spéciale. Doit être strictement positif.

    stat_defense_speciale : int
        Statistique de défense. Doit être strictement positif.
    """

    def __init__(
        self,
        id_: int,
        nom: str,
        types: tuple[str] | tuple[str, str],
        stat_pv: int,
        stat_attaque: int,
        stat_defense: int,
        stat_attaque_speciale: int,
        stat_defense_speciale: int,
    ):
        if not (isinstance(id_, int) and id_ > 0):
            raise ValueError("'id_' doit être un entier strictement positif.")

        if not isinstance(nom, str):
            raise TypeError("'nom' doit être une instance de str.")

        if not (isinstance(types, tuple) and len(types) in (1, 2) and all(type_ in TYPES for type_ in types)):
            raise TypeError("'types' doit être un t-uplet de longueur 1 ou 2 dont les éléments sont des types valides.")

        if not (isinstance(stat_pv, int) and stat_pv > 0):
            raise ValueError("'stat_pv' doit être un entier strictement positif.")

        if not (isinstance(stat_attaque, int) and stat_attaque > 0):
            raise ValueError("'stat_attaque' doit être un entier strictement positif.")

        if not (isinstance(stat_defense, int) and stat_defense > 0):
            raise ValueError("'stat_defense' doit être un entier strictement positif.")

        if not (isinstance(stat_attaque_speciale, int) and stat_attaque_speciale > 0):
            raise ValueError("'stat_attaque_speciale' doit être un entier strictement positif.")

        if not (isinstance(stat_defense_speciale, int) and stat_defense_speciale > 0):
            raise ValueError("'stat_defense_speciale' doit être un entier strictement positif.")

        self.__id_ = id_
        self.__nom = nom
        self.__types = types
        self.__stat_pv = stat_pv
        self.__stat_attaque = stat_attaque
        self.__stat_defense = stat_defense
        self.__stat_attaque_speciale = stat_attaque_speciale
        self.__stat_defense_speciale = stat_defense_speciale

    @property
    def _id_(self) -> int:
        return self.__id_

    @property
    def _nom(self) -> str:
        return self.__nom

    @property
    def _types(self) -> tuple[str] | tuple[str, str]:
        return self.__types

    @property
    def _stat_pv(self) -> int:
        return self.__stat_pv

    @property
    def _stat_attaque(self) -> int:
        return self.__stat_attaque

    @property
    def _stat_defense(self) -> int:
        return self.__stat_defense

    @property
    def _stat_attaque_speciale(self) -> int:
        return self.__stat_attaque_speciale

    @property
    def _stat_defense_speciale(self) -> int:
        return self.__stat_defense_speciale

    def __str__(self) -> str:
        return self.__nom
