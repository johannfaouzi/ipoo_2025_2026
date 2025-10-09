from abc import ABC, abstractmethod


class Courrier(ABC):
    """Classe mère abstraite pour les courriers.

    Parameters
    ----------
    destination : str
        Adresse de destination.

    source : str
        Adresse d'expédition.

    poids : int or float
        Le poids du courrier.

    mode : {'normal', 'rapide}
        Mode d'envoi.
    """

    def __init__(self, destination: str, source: str, poids: int | float, mode: str):
        if not isinstance(destination, str):
            raise TypeError("'destination' doit être une instance de str.")
        if not isinstance(source, str):
            raise TypeError("'source' doit être une instance de str.")
        if not isinstance(poids, (int, float)):
            raise TypeError("'poids' doit être une instance de int ou float.")
        if not poids > 0:
            raise ValueError("'poids' doit être strictement positif.")
        if mode not in ("normal", "rapide"):
            raise ValueError("'mode' doit être 'normal' ou 'rapide'.")

        self.destination = destination
        self.source = source
        self.poids = poids
        self.mode = mode

    @abstractmethod
    def _calcul_affranchissement_normal(self) -> float:
        """Calcul de l'affranchissement en tarif normal.

        Returns
        -------
        float
            L'affranchissement en tarif normal.
        """
        ...

    def calcul_affranchissement(self) -> float:
        """Calcul de l'affranchissement effectif.

        Returns
        -------
        float
            L'affranchissement à payer.
        """
        normal: float = self._calcul_affranchissement_normal()
        return round((2 * normal) if self.mode == "rapide" else normal, 2)

    @abstractmethod
    def _format_str(self) -> str:
        """Renvoie une chaîne décrivant le format du courrier.

        Returns
        -------
        str
            Le format.
        """
        ...

    def __str__(self) -> str:
        """Conversion en chaîne de caractères."""
        string: str = "\n".join(
            [
                f"{type(self).__name__}",
                f"  Adresse destination : {self.destination}",
                f"  Adresse expédition : {self.source}",
                f"  Poids : {self.poids} gramme{'s' if self.poids >= 2 else ''}",
                f"  Mode : {'rapide' if self.mode == 'rapide' else 'normal'}",
                f"  {self._format_str()}",
                f"  Prix du timbre : {self.calcul_affranchissement():.2f}€",
            ]
        )
        return string
