from .courrier import Courrier


class Lettre(Courrier):
    """Courrier de type lettre.

    Parameters
    ----------
    format_lettre : {'A3', 'A4'}
        Format de la lettre.

    Examples
    --------
    >>> lettre = Lettre('Paris', 'Rennes', 42, 'normal', 'A4')
    >>> lettre.calcul_affranchissement()
    2.54
    >>> print(lettre)
    Lettre
      Adresse destination : Paris
      Adresse expédition : Rennes
      Poids : 42 grammes
      Mode : normal
      Format : A4
      Prix du timbre : 2.54€
    """

    def __init__(self, destination: str, source: str, poids: int | float, mode: str, format_lettre: str):
        super().__init__(destination, source, poids, mode)
        if format_lettre not in ("A3", "A4"):
            raise ValueError("'format_lettre' doit être 'A3' ou 'A4'.")
        self.format_lettre = format_lettre

    def _calcul_affranchissement_normal(self) -> float:
        return self.poids / 1000 + (2.5 if self.format_lettre == "A4" else 3.5)

    def _format_str(self) -> str:
        """Renvoie le format spécifique à la classe Lettre."""
        return f"Format : {'A4' if self.format_lettre == 'A4' else 'A3'}"
