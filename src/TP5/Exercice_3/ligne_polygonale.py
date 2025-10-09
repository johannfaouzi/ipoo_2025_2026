from .point import Point


class LignePolygonale:
    """Représentation d'une ligne polygonale.

    Parameters
    ----------
    sommets : list[Point]
        La liste de sommets de la ligne polygonale.
    """

    def __init__(self, sommets: list[Point]) -> None:
        if not (isinstance(sommets, list) and all(isinstance(point, Point) for point in sommets) and len(sommets) >= 2):
            raise ValueError("'sommets' doit être une liste de points de longueur supérieure ou égal à 2.")
        self.__sommets = sommets
        self.__nb_sommets: int = len(sommets)

    def __str__(self) -> str:
        """Conversion en texte.

        Returns
        -------
        str
            Description textuelle de la ligne.

        Examples
        --------
        >>> ligne = LignePolygonale([Point(1, 2), Point(3, 4)])
        >>> print(ligne)
        (1, 2) - (3, 4)
        """
        return " - ".join(str(sommet) for sommet in self.__sommets)

    def get_sommet(self, i: int) -> Point:
        """Retourne un des sommets

        Parameters
        ----------
        i : int
            Index du sommet.

        Returns
        -------
        Point
            Le sommet demandé.

        Examples
        --------
        >>> ligne = LignePolygonale([Point(1, 2), Point(3, 4)])
        >>> print(ligne.get_sommet(1))
        (3, 4)
        """
        assert i < self.__nb_sommets
        return self.__sommets[i]

    def set_sommet(self, i: int, p: Point) -> None:
        """Change un des sommets.

        Parameters
        ----------
        i : int
            Index du sommet à changer.
        p : Point
            Nouveau point.

        Examples
        --------
        >>> ligne = LignePolygonale([Point(1, 2), Point(3, 4)])
        >>> ligne.set_sommet(0, Point(0, 0))
        >>> print(ligne)
        (0, 0) - (3, 4)
        """
        assert i < self.__nb_sommets
        self.__sommets[i] = p

    def homothetie(self, k: int | float) -> None:
        """Applique une homothétie

        Parameters
        ----------
        k : int or float
            Rapport d'homothétie.

        Examples
        --------
        >>> ligne = LignePolygonale([Point(1, 2), Point(3, 4)])
        >>> ligne.homothetie(2)
        >>> print(ligne)
        (2, 4) - (6, 8)
        """
        for s in self.__sommets:
            s.homothetie(k)

    def translation(self, dx: int | float, dy: int | float) -> None:
        """Applique une translation

        Parameters
        ----------
        dx : int or float
            La translation selon l'axe des abscisses.
        dy : int or float
            La translation selon l'axe des ordonnées.

        Examples
        --------
        >>> ligne = LignePolygonale([Point(1, 2), Point(3, 4)])
        >>> ligne.translation(2, -2)
        >>> print(ligne)
        (3, 0) - (5, 2)
        """
        for s in self.__sommets:
            s.translation(dx, dy)

    def rotation(self, a: int | float) -> None:
        """Applique une rotation par rapport à l'origine.

        Parameters
        ----------
        a : float
            L'angle de rotation.

        Examples
        --------
        >>> ligne = LignePolygonale([Point(1.5, 2.5), Point(3.8, 4.2)])
        >>> ligne.rotation(3.14)
        >>> print(ligne)
        (-1..., -2...) - (-3..., -4...)
        """
        for s in self.__sommets:
            s.rotation(a)
