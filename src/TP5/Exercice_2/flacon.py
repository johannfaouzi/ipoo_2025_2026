class Flacon:
    """Un flacon de sirop dilué dans de l'eau.

    Parameters
    ----------
    etiquette : str
        L'étiquette du flacon.

    capacite : int
        Sa capacité en millilitres.

    Attributes
    ----------
    volume : int | float
        Le volume de liquide contenu en millilitres.

    concentration : float
        La concentration en sirop dans le flacon.

    Examples
    --------
    >>> flacon1 = Flacon("Sirop", 1000)
    >>> flacon2 = Flacon("Sirop", 500)
    >>> flacon1.remplir(200, 600)
    True
    >>> flacon2.remplir(100, 400)
    True
    >>> flacon1.transvaser(flacon2, 800)
    False
    >>> flacon1.transvaser(flacon2, 400)
    False
    >>> flacon1.transvaser(flacon2, 200)
    True
    >>> flacon1.concentration
    0.24
    """

    def __init__(self, etiquette: str, capacite: int) -> None:
        self.etiquette = etiquette
        self.capacite = capacite
        self.volume: int | float = 0
        self.concentration: float = 0.0

    def __str__(self) -> str:
        """Convertir en chaîne de caractères.

        Returns
        -------
        str
            Description du flacon et de son contenu

        Examples
        --------
        >>> flacon = Flacon("Sirop", 1000)
        >>> print(flacon)
        Flacon "Sirop", 1000mL, rempli de 0mL concentré à 0%.
        >>> flacon.remplir(10, 90)
        True
        >>> print(flacon)
        Flacon "Sirop", 1000mL, rempli de 100mL concentré à 10%.
        """
        return (
            f'Flacon "{self.etiquette}", {self.capacite}mL, '
            f"rempli de {self.volume}mL concentré à {self.concentration:.0%}."
        )

    def remplir(self, volume_sirop: int | float, volume_eau: int | float) -> bool:
        """Ajoute du sirop et de l'eau dans le flacon.

        Parameters
        ----------
        volume_sirop : int or float
            Volume de sirop en millilitres.

        volume_eau : int or float
            Volume d'eau en millilitres.

        Returns
        -------
        bool
            True si la capacité n'est pas dépassée (sinon, l'opération est annulée).

        Examples
        --------
        >>> flacon = Flacon("Sirop", 1000)
        >>> flacon.remplir(20, 180)
        True
        >>> flacon.remplir(0, 900)
        False
        >>> flacon.concentration
        0.1
        """
        if volume_sirop < 0 or volume_eau < 0:
            return False

        nouveau_volume: int | float = volume_eau + volume_sirop + self.volume
        if nouveau_volume > self.capacite:
            return False

        self.concentration = (self.volume * self.concentration + volume_sirop) / nouveau_volume
        self.volume = nouveau_volume
        return True

    def transvaser(self, autre_flacon: "Flacon", volume: int | float) -> bool:
        """Transvase d'un flacon à l'autre.

        Mets à jour la concentration dans le flacon.

        Parameters
        ----------
        autre_flacon : Flacon
            Le flacon utilisé

        volume : int or float
            le volume à extraire de autre_flacon

        Returns
        -------
        bool
            True si l'opération a réussi (sinon, l'opération est annulée).

        Examples
        --------
        >>> flacon1 = Flacon("Sirop", 1000)
        >>> flacon2 = Flacon("Sirop", 500)
        >>> flacon2.remplir(100, 400)
        True
        >>> flacon1.transvaser(flacon2, 800)
        False
        >>> flacon1.transvaser(flacon2, 400)
        True
        >>> flacon1.volume
        400.0
        >>> flacon2.volume
        100
        """
        if autre_flacon.volume < volume or self.capacite - self.volume < volume:
            return False

        sirop: float = volume * autre_flacon.concentration
        eau: float = volume - sirop

        autre_flacon.volume -= volume
        self.remplir(sirop, eau)

        return True
