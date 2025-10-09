from typing import Any


class Complexe:
    """Nombre complexe.

    Parameters
    ----------
    reelle : int | float
        Partie réelle.

    imaginaire : int | float
        Partie imaginaire.

    Examples
    --------
    >>> c1 = Complexe(1, 1)
    >>> c2 = Complexe(2, -3)
    >>> print(c1 + c2)
    3 - 2i
    >>> print(c1 + (2 -3j))
    3.0 - 2.0i
    >>> print(c1 + 2)
    3 + 1i
    >>> print(c1 - c2)
    -1 + 4i
    >>> print(c1 - (2 -3j))
    -1.0 + 4.0i
    >>> c1 * c2
    Complexe(5, -1)
    >>> c1 * (2 - 3j)
    Complexe(5.0, -1.0)
    >>> c1 * 3
    Complexe(3, 3)
    """

    def __init__(self, reelle: int | float, imaginaire: int | float) -> None:
        self.reelle = reelle
        self.imaginaire = imaginaire

    def __add__(self, other: Any) -> "Complexe":
        if isinstance(other, Complexe):
            return Complexe(self.reelle + other.reelle, self.imaginaire + other.imaginaire)
        elif isinstance(other, complex):
            return Complexe(self.reelle + other.real, self.imaginaire + other.imag)
        elif isinstance(other, (int, float)):
            return Complexe(self.reelle + other, self.imaginaire)
        else:
            return NotImplemented

    def __sub__(self, other: Any) -> "Complexe":
        if isinstance(other, Complexe):
            return Complexe(self.reelle - other.reelle, self.imaginaire - other.imaginaire)
        elif isinstance(other, complex):
            return Complexe(self.reelle - other.real, self.imaginaire - other.imag)
        elif isinstance(other, (int, float)):
            return Complexe(self.reelle - other, self.imaginaire)
        else:
            return NotImplemented

    def __mul__(self, other: Any) -> "Complexe":
        if isinstance(other, Complexe):
            return Complexe(
                self.reelle * other.reelle - self.imaginaire * other.imaginaire,
                self.imaginaire * other.reelle + self.reelle * other.imaginaire,
            )
        elif isinstance(other, complex):
            return Complexe(
                self.reelle * other.real - self.imaginaire * other.imag,
                self.imaginaire * other.real + self.reelle * other.imag,
            )
        elif isinstance(other, (int, float)):
            return Complexe(self.reelle * other, self.imaginaire * other)
        else:
            return NotImplemented

    def __str__(self) -> str:
        return f"{self.reelle} {'+' if self.imaginaire >= 0 else '-'} {abs(self.imaginaire)}i"

    def __repr__(self) -> str:
        return f"Complexe({self.reelle}, {self.imaginaire})"
