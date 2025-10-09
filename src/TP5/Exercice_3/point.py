"""Classe modélisant un point."""

from math import atan2, cos, sin, sqrt
from typing import Any


class Point:
    """Construit un point.

    Parameters
    ----------
    x : int or float
        Abscisse du point.

    y : int or float
        Ordonnée du point.
    """

    def __init__(self, x: int | float, y: int | float) -> None:
        self.__x = x
        self.__y = y

    def __str__(self) -> str:
        """Représentation textuelle du point

        Returns
        -------
        str
            Description du point.

        Examples
        --------
        >>> print(Point(1, 2))
        (1, 2)
        >>> print(Point(-2., 3.))
        (-2.0, 3.0)
        """
        return f"({self.__x}, {self.__y})"

    def __eq__(self, other: Any) -> bool:
        """Teste l'égalité de deux points.

        Parameters
        ----------
        autre_point : Point
            L'autre point à tester.

        Returns
        -------
        bool
            True si et seulement si les coordonnées correspondent.

        Examples
        --------
        >>> Point(1, 2) == Point(1., 2.)
        True
        >>> Point(1, 2) == Point(2, 1)
        False
        """
        if isinstance(other, Point):
            return (self.__x == other.__x) and (self.__y == other.__y)
        return NotImplemented

    @property
    def x(self) -> int | float:
        """Renvoie l'abscisse.

        Returns
        -------
        float
            Abscisse du point.

        Examples
        --------
        >>> Point(1, 2).x
        1
        """
        return self.__x

    @property
    def y(self) -> int | float:
        """Renvoie l'ordonnée.

        Returns
        -------
        float
            Ordonée du point.

        Examples
        --------
        >>> Point(1, 2).y
        2
        """
        return self.__y

    @property
    def r(self) -> float:
        """Renvoie le rayon en coordonnées polaires.

        Returns
        -------
        float
            Distance à l'origine.

        Examples
        --------
        >>> Point(3, 4).r
        5.0
        """
        return sqrt(self.__x**2 + self.__y**2)

    @property
    def t(self) -> float:
        """Renvoie l'angle en coordonnées polaires

        Returns
        -------
        float
            Angle avec l'axe des abscisses.

        Examples
        --------
        >>> Point(0, 0).t
        0.0
        >>> Point(1, 1).t
        0.7853...
        >>> Point(2, 2).t
        0.7853...
        """
        return atan2(self.__y, self.__x)

    def homothetie(self, k: int | float) -> None:
        """Applique une homothétie au point.

        Parameters
        ----------
        k : int or float
            Le rapport d'homothétie à appliquer.

        Examples
        --------
        >>> point = Point(1, 2)
        >>> point.homothetie(2)
        >>> print(point)
        (2, 4)
        """
        self.__x *= k
        self.__y *= k

    def translation(self, dx: int | float, dy: int | float) -> None:
        """Applique une translation.

        Parameters
        ----------
        dx : int or float
            La translation selon l'axe des abscisses.

        dy : int or float
            La translation selon l'axe des ordonnées.

        Examples
        --------
        >>> point = Point(1, 2)
        >>> point.translation(-1, 3)
        >>> print(point)
        (0, 5)
        """
        self.__x += dx
        self.__y += dy

    def rotation(self, a: int | float) -> None:
        """Applique une rotation par rapport à l'origine.

        Parameters
        ----------
        a : int or float
            L'angle de rotation.

        Examples
        --------
        >>> point = Point(1.5, 2.5)
        >>> point.rotation(3.14)
        >>> print(point)
        (-1..., -2...)
        """
        t = self.t + a
        self.__x = self.r * cos(t)
        self.__y = self.r * sin(t)
