from ..Exercice_3.point import Point


class Rectangle:
    """Crée un rectangle à partir des coordonnées de ses points.

    Parameters
    ----------
    x0 : int or float
        abscisse du premier point

    y0 : int or float
        ordonnée du premier point

    x1 : int or float
        abscisse du deuxième point

    y1 : int or float
        ordonnée du deuxième point

    Attributes
    ----------
    coin_no : Point
        Coin nord-ouest du rectangle.

    coin_se : Point
        Coin sud-est du rectangle.

    Examples
    --------
    >>> rectangle = Rectangle(1, 2, 3, 4)
    >>> print(rectangle)
    [(1, 2) ; (3, 4)]
    """

    def __init__(self, x0: int | float, y0: int | float, x1: int | float, y1: int | float) -> None:
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.coin_no: Point = Point(x0, y0)
        self.coin_se: Point = Point(x1, y1)

    def __str__(self) -> str:
        """Représentation textuelle du rectangle.

        Returns
        -------
        str
            Description du rectangle.

        Examples
        --------
        >>> rectangle = Rectangle(1, 2, 3, 4)
        >>> print(rectangle)
        [(1, 2) ; (3, 4)]
        """
        return f"[{self.coin_no} ; {self.coin_se}]"
