from typing import Any

from .types import TYPES


class Attaque:
    """Attaque.

    Cette classe contient toutes les informations d'une attaque.

    Parameters
    ----------
    nom : str
        Nom de l'attaque.

    description : str
        Description del'attaque.

    points_pouvoir : int
        Points de pouvoir de l'attaque. Doit être strictement positif.

    type_ : str
        Type de l'attaque.

    classe : {'statut', 'physique', 'spéciale'}
        Classe de l'attaque.

    puissance : int or None
        Puissance de l'attaque. Doit être None si classe == 'statut', sinon un entier stricement positif.

    stat_modifiee : str or None
        Statistique modifiée. Doit être l'un de 'attaque', 'defense', 'attaque_speciale', 'defense_speciale'
        si classe == 'statut', sinon None.

    stat_niveau : int or None
        Le changement de niveau de la stat. Doit être -2, -1, 1 ou 2 si classe == 'statut', sinon None.

    stat_pokemon : {'attaquant', 'attaqué'} or None
        Le Pokémon dont la statistique est modifiée.

    Examples
    --------
    >>> morsure = Attaque(
    ...     nom='Morsure',
    ...     description="L'ennemi est mordu par de tranchantes canines.",
    ...     points_pouvoir=25,
    ...     type_='TENEBRES',
    ...     classe='physique',
    ...     puissance=60,
    ...     stat_modifiee=None,
    ...     stat_niveau=None,
    ...     stat_pokemon=None
    ... )
    >>> lance_flammes = Attaque(
    ...     nom='Lance-Flammes',
    ...     description="L'ennemi reçoit un torrent de flammes.",
    ...     points_pouvoir=15,
    ...     type_='FEU',
    ...     classe='spéciale',
    ...     puissance=90,
    ...     stat_modifiee=None,
    ...     stat_niveau=None,
    ...     stat_pokemon=None
    ... )
    >>> morsure == lance_flammes
    False
    """

    def __init__(
        self,
        nom: str,
        description: str,
        points_pouvoir: int,
        type_: str,
        classe: str,
        puissance: int,
        stat_modifiee: str | None,
        stat_niveau: int | None,
        stat_pokemon: str | None,
    ):
        if not isinstance(nom, str):
            raise TypeError("'nom' doit être une instance de str.")

        if not isinstance(description, str):
            raise TypeError("'description' doit être une instance de str.")

        if not (isinstance(points_pouvoir, int) and points_pouvoir > 0):
            raise ValueError("'points_pouvoir' doit être un entier strictement positif.")

        if type_ not in TYPES:
            raise ValueError("'type_' doit être un type valide.")

        if classe not in ("statut", "physique", "spéciale"):
            raise ValueError("'classe' doit être l'un de 'statut', 'physique' ou 'spéciale'.")

        if classe == "statut":
            if puissance is not None:
                raise TypeError("Si classe='statut', puissance doit être None.")
        else:
            if not (isinstance(puissance, int) and puissance > 0):
                raise ValueError(
                    "Si classe='physique' ou classe='spéciale', 'puissance' doit être un entier strictement positif."
                )

        if classe == "statut":
            if stat_modifiee not in ("attaque", "defense", "attaque_speciale", "defense_speciale"):
                raise ValueError(
                    "Si classe='statut', 'stat_modifiee' doit être l'un de "
                    "'attaque', 'defense', 'attaque_speciale' ou 'defense_speciale'."
                )
        else:
            if stat_modifiee is not None:
                raise TypeError("Si classe='physique' ou classe='spéciale', 'stat_modifiee' doit être None.")

        if classe == "statut":
            if stat_niveau not in (-2, -1, 1, 2):
                raise ValueError("Si classe='statut', 'stat_niveau' doit être l'un de -2, -1, 0, 1 ou 2.")
        else:
            if stat_niveau is not None:
                raise TypeError("Si classe='physique' ou classe='spéciale', 'stat_niveau' doit être None.")

        if classe == "statut":
            if stat_pokemon not in ("attaquant", "attaqué"):
                raise ValueError("Si classe='statut', 'stat_pokemon' doit être l'un de 'attaquant' ou 'attaqué'.")
        else:
            if stat_pokemon is not None:
                raise TypeError("Si classe='physique' ou classe='spéciale', 'stat_pokemon' doit être None.")

        self.__nom = nom
        self.__description = description
        self.__points_pouvoir = points_pouvoir
        self.__type_ = type_
        self.__classe = classe
        self.__puissance = puissance
        self.__stat_modifiee = stat_modifiee
        self.__stat_niveau = stat_niveau
        self.__stat_pokemon = stat_pokemon

    @property
    def nom(self) -> str:
        return self.__nom

    @property
    def description(self) -> str:
        return self.__description

    @property
    def points_pouvoir(self) -> int:
        return self.__points_pouvoir

    @property
    def type_(self) -> str:
        return self.__type_

    @property
    def classe(self) -> str:
        return self.__classe

    @property
    def puissance(self) -> int:
        return self.__puissance

    @property
    def stat_modifiee(self) -> str | None:
        return self.__stat_modifiee

    @property
    def stat_niveau(self) -> int | None:
        return self.__stat_niveau

    @property
    def stat_pokemon(self) -> str | None:
        return self.__stat_pokemon

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Attaque):
            return self.__nom == other.__nom
        return NotImplemented

    def __repr__(self) -> str:
        string: str = (
            f"Attaque(nom={self.__nom!r}, description={self.__description!r}, points_pouvoir={self.__points_pouvoir!r},"
            f" type_={self.__type_!r}, classe={self.__classe!r}, puissance={self.__puissance!r},"
            f" stat_modifiee={self.__stat_modifiee!r}, stat_niveau={self.__stat_niveau!r},"
            f" stat_pokemon={self.__stat_pokemon!r})"
        )
        return string

    def __hash__(self) -> int:
        return hash(repr(self))

    def decremente_points_pouvoir(self) -> None:
        """Décrémente de 1 les points de pouvoir de l'attaque."""
        self.__points_pouvoir -= 1
