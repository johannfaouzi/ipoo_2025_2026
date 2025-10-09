class Domino:
    """Domino d'un jeu de dominos.

    Parameters
    ----------
    extr_A: int
        Extrémité A du domino.

    extr_B: int
        Extrémité B du domino.

    Examples
    --------
    >>> d1 = Domino(2, 6)
    >>> d2 = Domino(4, 3)
    >>> print(d1)
    [2|6]
    >>> print(d2)
    [4|3]
    >>> d1.valeur()
    8
    >>> d2.valeur()
    7
    >>> print(d1.retourne())
    [6|2]
    >>> d1.accepte_apres(d2)
    False
    """

    def __init__(self, extr_A: int, extr_B: int) -> None:
        self.extr_A = extr_A
        self.extr_B = extr_B

    def __str__(self) -> str:
        """Converti le domino en chaîne de caractères

        Returns
        -------
        str

        Examples
        --------
        >>> d1 = Domino(2, 6)
        >>> print(d1)
        [2|6]
        """
        return f"[{self.extr_A}|{self.extr_B}]"

    def valeur(self) -> int:
        """Retourne la somme des valeurs du domino

        Returns
        -------
        int
            la somme des extrémités

        Examples
        --------
        >>> d1 = Domino(2, 6)
        >>> d1.valeur()
        8
        """
        return self.extr_A + self.extr_B

    def retourne(self) -> "Domino":
        """Retourne la somme des valeurs du domino

        Returns
        -------
        int
            la somme des extrémités

        Examples
        --------
        >>> d1 = Domino(2, 6)
        >>> print(d1.retourne())
        [6|2]
        """
        self.extr_A, self.extr_B = self.extr_B, self.extr_A
        return self

    def accepte_apres(self, other: "Domino") -> bool:
        """Vérifie si l'autre domino peut être posé après ce domino.

        Parameters
        ----------
        other : Domino
            Un autre domino.

        Returns
        -------
        bool
            Si l'autre domino peut être posé après ce domino.

        Examples
        --------
        >>> d1 = Domino(2, 6)
        >>> d2 = Domino(4, 3)
        >>> d3 = Domino(6, 3)
        >>> d1.accepte_apres(d2)
        False
        >>> d1.accepte_apres(d3)
        True
        >>> d2.accepte_apres(d3)
        True
        """
        return self.extr_B in (other.extr_A, other.extr_B)
