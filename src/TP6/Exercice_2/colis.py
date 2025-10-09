from .courrier import Courrier


class Colis(Courrier):
    """Courrier de type colis.

    Parameters
    ----------
    volume : float
        le volume occupé par le colis

    Examples
    --------
    >>> colis = Colis('Paris', 'Rennes', 42, 'normal', 0.2)
    >>> colis.calcul_affranchissement()
    0.09
    >>> print(colis)
    Colis
      Adresse destination : Paris
      Adresse expédition : Rennes
      Poids : 42 grammes
      Mode : normal
      Volume : 0.20 litre
      Prix du timbre : 0.09€
    """

    def __init__(self, destination: str, source: str, poids: int | float, mode: str, volume: int | float):
        super().__init__(destination, source, poids, mode)
        if not isinstance(volume, (int, float)):
            raise TypeError("'volume' doit être une instance de int ou float.")
        if not volume > 0:
            raise ValueError("'volume' doit être strictement positif.")
        self.volume = volume

    def _calcul_affranchissement_normal(self) -> float:
        return self.poids / 1000 + self.volume / 4

    def _format_str(self) -> str:
        """Renvoie le format spécifique à la classe Colis."""
        return f"Volume : {self.volume:.2f} " f"litre{'s' if self.volume >= 2 else ''}"
