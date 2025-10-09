from __future__ import annotations

from .attaque import Attaque
from .base_pokemon import BasePokemon
from .dict_attaques import DICT_ATTAQUES
from .types import TYPE_EFFICACITE


class Pokemon(BasePokemon):
    """Classe d'un Pokémon spécifique.

    Parameters
    ----------
    id_ : int
        Identifiant du Pokémon (numéro dans le Pokédex).
        Doit être strictement positif.

    nom : str
        Nom du Pokémon.

    types : tuple[str]
        Type(s) du Pokémon. Si le Pokémon n'a qu'un type, le tuple est
        de longeur 1, sinon de longueur 2.

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

    niveau : int
        Niveau du Pokémon. Doit être compris entre 1 et 100 inclus.

    liste_attaques : list[Attaque]
        Liste contenant les 4 attaques du Pokémon.

    """

    # Correspondance entre niveau et facteur multiplicatif
    __CORRESPONDANCE_NIVEAU_FACTEUR = {
        -6: 0.25,
        -5: 2.0 / 7.0,
        -4: 1.0 / 3.0,
        -3: 0.4,
        -2: 0.5,
        -1: 2.0 / 3.0,
        0: 1.0,
        1: 1.5,
        2: 2.0,
        3: 2.5,
        4: 3.0,
        5: 3.5,
        6: 4.0,
    }

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
        niveau: int,
        liste_attaques: list[Attaque],
    ):

        super().__init__(
            id_, nom, types, stat_pv, stat_attaque, stat_defense, stat_attaque_speciale, stat_defense_speciale
        )

        if not (isinstance(niveau, int) and (1 <= niveau <= 100)):
            raise TypeError("'niveau' doit être un entier compris entre 1 et 100 inclus.")

        if not (
            isinstance(liste_attaques, list)
            and (len(liste_attaques) == len(set(liste_attaques)) == 4)
            and all(isinstance(attaque, Attaque) and attaque.nom in DICT_ATTAQUES for attaque in liste_attaques)
        ):
            raise ValueError(
                "'liste_attaques' doit être une liste de longueur 4 dont tous les éléments sont des attaques uniques "
                "et présentes dans la base de données."
            )

        self.__niveau = niveau
        self.__liste_attaques = liste_attaques

        self.__base_pv = int(0.02 * self.__niveau * self._stat_pv) + self.__niveau + 10
        self.__base_attaque = self.__calcule_base_stat(self._stat_attaque)
        self.__base_defense = self.__calcule_base_stat(self._stat_defense)
        self.__base_attaque_speciale = self.__calcule_base_stat(self._stat_attaque_speciale)
        self.__base_defense_speciale = self.__calcule_base_stat(self._stat_defense_speciale)

        self.__pv_effectif = self.__base_pv
        self.__niveau_attaque = 0
        self.__niveau_defense = 0
        self.__niveau_attaque_speciale = 0
        self.__niveau_defense_speciale = 0

    def __calcule_base_stat(self, stat: int) -> int:
        """Calcule la statistique de base du Pokémon (sauf les PV).

        Parameters
        ----------
        stat : int
            Valeur générale de la statistique.

        Returns
        -------
        int
            Valeur de la statistique du Pokémon.
        """
        return int(0.02 * self.__niveau * stat) + 5

    def __calcule_stat_effective(self, stat: str) -> float:
        """Calcule la valeur effective d'une statistique.

        Parameters
        ----------
        stat : {'attaque', 'defense', 'attaque_speciale', 'defense_speciale'}
            Statistique considérée.

        Returns
        -------
        float
            Statistique effective.

        """
        if stat == "attaque":
            return self.__base_attaque * self.__CORRESPONDANCE_NIVEAU_FACTEUR[self.__niveau_attaque]
        elif stat == "defense":
            return self.__base_defense * self.__CORRESPONDANCE_NIVEAU_FACTEUR[self.__niveau_defense]
        elif stat == "attaque_speciale":
            return self.__base_attaque_speciale * self.__CORRESPONDANCE_NIVEAU_FACTEUR[self.__niveau_attaque_speciale]
        elif stat == "defense_speciale":
            return self.__base_defense_speciale * self.__CORRESPONDANCE_NIVEAU_FACTEUR[self.__niveau_defense_speciale]
        else:
            raise ValueError("La valeur de 'stat' n'est pas correcte.")

    def __calcule_multiplicateur_stab(self, attaque: Attaque) -> float:
        """Calcule le facteur multiplicatif lié aux types.

        Ce facteur multiplicatif dépend du type de l'attaque et du type (ou des types) du Pokémon attaquant. Il vaut
        1.5 si le type de l'attaque fait partie des types du Pokémon et 1.0 sinon. STAB est l'acronyme de Same Type
        Attack Bonus.

        Parameters
        ----------
        attaque : Attaque
            Attaque du Pokémon attaquant.

        Returns
        -------
        float
            Facteur multiplicatif.
        """
        return 1.5 if attaque.type_ in self._types else 1.0

    @staticmethod
    def __calcule_multiplicateur_type(attaque: Attaque, pokemon: "Pokemon") -> float:
        """Calcule le facteur multiplicatif lié aux types.

        Ce facteur multiplicatif dépend du type de l'attaque et du type (ou des types) du Pokémon attaqué.

        Parameters
        ----------
        attaque : Attaque
            Attaque du Pokémon attaquant.

        pokemon : Pokemon
            Pokémon attaqué.

        Returns
        -------
        float
            Facteur multiplicatif.
        """
        res: float = 1.0
        for type_ in pokemon._types:
            if type_ in TYPE_EFFICACITE[attaque.type_]:
                res *= TYPE_EFFICACITE[attaque.type_][type_]
        return round(res, 2)

    @staticmethod
    def __calcule_degats(
        niveau: int,
        puissance: int,
        attaque: float,
        defense: float,
        multiplicateur_stab: float,
        multiplicateur_type: float,
    ) -> int:
        """Calcule les dégâts effectués par l'attaque.

        Parameters
        ----------
        niveau : int
            Niveau du Pokémon qui attaque.

        puissance : int
            Puissance de l'attaque.

        attaque : float
            Attaque (spéciale) du Pokémon attaquant.

        defense : float
            Défense (spéciale) du Pokémon attaqué.

        multiplicateur_stab : float
            Multiplicateur du bonus d'attaque du même type pour le Pokémon attaquant.

        multiplicateur_type : float
            Multiplicateur lié aux types de l'attaque et du Pokémon attaqué.

        Returns
        -------
        degats : int
            Dégâts de l'attaque.
        """
        degats: int = round(
            ((0.4 * niveau + 2) * puissance * attaque / (defense * 50) + 2) * multiplicateur_stab * multiplicateur_type
        )
        return degats

    @staticmethod
    def __clip(x: int, a: int, b: int) -> int:
        """Renvoie la plus proche valeur de x contenue dans l'intervalle [a, b].

        Parameters
        ----------
        x : int
            La valeur initiale.

        a : int
            La valeur minimale de la nouvelle valeur.

        b : int
            La valeur maximale de la nouvelle valeur.

        Returns
        -------
        int
            L'entier le plus proche valeur de x contenu dans l'intervalle [a, b].
        """
        return min(max(x, a), b)

    def __change_niveau_stat(self, attaque: Attaque, pokemon: "Pokemon | None" = None) -> None:
        """Change le niveau d'une statistique d'un Pokémon.

        Parameters
        ----------
        attaque : Attaque
            Attaque utilisée.

        pokemon : Pokemon or None
            Le Pokémon dont le niveau de la statistique est modifiée. Si None, l'objet courant (self) est utilisé.
        """
        if pokemon is None:
            pokemon = self
        assert attaque.stat_niveau is not None
        if attaque.stat_modifiee == "attaque":
            pokemon.__niveau_attaque = self.__clip(pokemon.__niveau_attaque + attaque.stat_niveau, -6, 6)
        elif attaque.stat_modifiee == "defense":
            pokemon.__niveau_defense = self.__clip(pokemon.__niveau_defense + attaque.stat_niveau, -6, 6)
        elif attaque.stat_modifiee == "attaque_speciale":
            pokemon.__niveau_attaque_speciale = self.__clip(
                pokemon.__niveau_attaque_speciale + attaque.stat_niveau, -6, 6
            )
        else:
            pokemon.__niveau_defense_speciale = self.__clip(
                pokemon.__niveau_defense_speciale + attaque.stat_niveau, -6, 6
            )

    def attaque(self, nom_attaque: str, other: "Pokemon") -> None:
        """Attaque un autre Pokémon avec l'attaque spécifiée.

        Parameters
        ----------
        nom_attaque : str
            Nom de l'attaque à utiliser.

        other : Pokémon
            Pokémon subissant l'attaque.
        """
        liste_nom_attaques = [attaque.nom for attaque in self.__liste_attaques]
        if nom_attaque not in liste_nom_attaques:
            raise ValueError(f"{self} ne connait pas l'attaque {nom_attaque}.")
        attaque = self.__liste_attaques[liste_nom_attaques.index(nom_attaque)]

        if self.__pv_effectif == 0:
            raise Exception(f"{self} est K.O. et ne peut donc pas attaquer.")
        if other.__pv_effectif == 0:
            raise Exception(f"{other} est K.O. et ne peut donc pas être attaqué.")
        if attaque.points_pouvoir == 0:
            raise Exception("Cette attaque n'a plus de points de pouvoir. Veuillez utiliser une autre attaque.")

        if attaque.classe == "statut":
            if attaque.stat_pokemon == "attaquant":
                self.__change_niveau_stat(attaque, self)
            else:
                self.__change_niveau_stat(attaque, other)
        else:
            if attaque.classe == "physique":
                attaque_pokemon_attaquant = self.__calcule_stat_effective("attaque")
                defense_pokemon_attaque = other.__calcule_stat_effective("defense")
            else:
                attaque_pokemon_attaquant = self.__calcule_stat_effective("attaque_speciale")
                defense_pokemon_attaque = other.__calcule_stat_effective("defense_speciale")

            multiplicateur_stab = self.__calcule_multiplicateur_stab(attaque)

            multiplicateur_type = self.__calcule_multiplicateur_type(attaque, other)

            degats = self.__calcule_degats(
                self.__niveau,
                attaque.puissance,
                attaque_pokemon_attaquant,
                defense_pokemon_attaque,
                multiplicateur_stab,
                multiplicateur_type,
            )

            other.__pv_effectif = max(0, other.__pv_effectif - degats)

        # Décrémente de 1 les points de pouvoir de l'attaque
        attaque.decremente_points_pouvoir()

        # Message à afficher
        string = f"{self} utilise {attaque.nom}."
        if attaque.classe == "statut":
            assert attaque.stat_modifiee is not None
            assert attaque.stat_niveau is not None
            mapping = {
                "attaque": "L'attaque",
                "defense": "La défense",
                "attaque_speciale": "L'attaque spéciale",
                "defense_speciale": "La défense spéciale",
            }
            string += (
                f" {mapping[attaque.stat_modifiee]} "
                f"de {self._nom if attaque.stat_pokemon == 'attaquant' else other._nom} "
                f"{'augmente' if attaque.stat_niveau > 0 else 'diminue'}"
                f"{' beaucoup' if abs(attaque.stat_niveau) == 2 else ''}."
            )
        else:
            if multiplicateur_type is not None:
                if round(multiplicateur_type) > 1:
                    string += " C'est super efficace."
                elif round(multiplicateur_type) < 1:
                    string += " Ce n'est pas très efficace."
        if other.__pv_effectif == 0:
            string += f" {other} est K.O."
        else:
            string += f" {other} a {other.__pv_effectif} PV restants."
        print(string)
