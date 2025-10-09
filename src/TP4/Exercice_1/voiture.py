class Voiture:
    """Définition d'une voiture.

    Parameters
    ----------
    nom : str
        Nom de la voiture.
    couleur : str
        Couleur de la voiture.
    vitesse : int (default = 0)
        Vitesse actuelle de la voiture.

    Examples
    --------
    >>> a1 = Voiture('titine', 'bleue')
    >>> a2 = Voiture('quatrelle','verte')
    >>> a3 = Voiture('bovelo','jaune')
    >>> a2.accelere(10)
    >>> a3.accelere(8)
    >>> print(a1)
    Voiture titine de couleur bleue à l'arrêt.
    >>> print(a2)
    Voiture quatrelle de couleur verte roule à 10km/h.
    >>> print(a3)
    Voiture bovelo de couleur jaune roule à 8km/h.
    """

    def __init__(self, nom: str, couleur: str, vitesse: int = 0) -> None:
        self.couleur = couleur
        self.nom = nom
        self.vitesse = vitesse

    def accelere(self, increment: int) -> None:
        """Augmente la vitesse de la voiture

        Vitesse max = 130km/h, augmentation max = 10km/h.

        Parameters
        ----------
        increment : int
            accélération

        Examples
        ---------
        >>> a1 = Voiture('titine', 'bleue')
        >>> a1.accelere(10)
        >>> print(a1)
        Voiture titine de couleur bleue roule à 10km/h.
        >>> a1.accelere(7)
        >>> print(a1)
        Voiture titine de couleur bleue roule à 17km/h.
        """
        if not (isinstance(increment, int) and 0 <= increment <= 10):
            raise ValueError("L'incrément doit être un entier compris entre 0 et 10 inclus.")
        if not (self.vitesse + increment <= 130):
            raise ValueError(
                f"La vitesse actuelle est de {self.vitesse}km/h. Il n'est pas possible d'acclérer de {increment}km/h "
                f"car la vitesse de la voiture ne doit pas dépasser 130km/h."
            )
        self.vitesse += increment

    def freine(self, decrement: int) -> None:
        """Diminue la vitesse de la voiture

        Vitesse min = 0km/h

        Parameters
        ----------
        decrement : int
            décélération

        Examples
        ---------
        >>> a1 = Voiture('titine', 'bleue')
        >>> a1.accelere(10)
        >>> a1.freine(8)
        >>> print(a1)
        Voiture titine de couleur bleue roule à 2km/h.
        >>> a1.freine(10)
        >>> print(a1)
        Voiture titine de couleur bleue à l'arrêt.
        """
        if not (isinstance(decrement, int) and 0 <= decrement):
            raise ValueError("Le décrément doit être un entier positif ou nul.")
        self.vitesse = max(0, self.vitesse - decrement)

    def est_arretee(self) -> bool:
        """La voiture est-elle à l'arrêt ?

        Returns
        -------
        bool
            True si elle est à 0km/h

        Examples
        ---------
        >>> a1 = Voiture('titine', 'bleue')
        >>> a1.est_arretee()
        True
        >>> a1.accelere(3)
        >>> a1.est_arretee()
        False
        """
        return self.vitesse == 0

    def __str__(self) -> str:
        """Convertit la voiture en chaîne de caractères

        Examples
        ---------
        >>> a1 = Voiture('titine', 'bleue')
        >>> print(a1)
        Voiture titine de couleur bleue à l'arrêt.
        """
        vitesse_str: str
        if self.est_arretee():
            vitesse_str = "à l'arrêt"
        else:
            vitesse_str = f"roule à {self.vitesse}km/h"

        return f"Voiture {self.nom} de couleur {self.couleur} {vitesse_str}."
