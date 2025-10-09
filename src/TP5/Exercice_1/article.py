from typing import Any


class Article:
    """Article d'un supermarché.

    Parameters
    ----------
    reference : int
        référence de l'article

    intitule : str
        intitulé de l'article

    prix_ht : float
        prix hors taxes

    quantite_en_stock : int
        quantité en stock de l'article

    Examples
    --------
    >>> article1 = Article(123, "pomme", 0.40, 12)
    >>> article2 = Article(126, "poire", 0.30, 8)
    >>> article1 == article2
    False
    >>> article2 < article1
    True
    >>> article2.approvisionner(8)
    >>> article1 < article2
    True
    >>> article2.vendre(8)
    >>> article2 < article1
    True
    """

    def __init__(self, reference: int, intitule: str, prix_ht: float, quantite_en_stock: int) -> None:
        self.reference = reference
        self.intitule = intitule
        self.prix_ht = prix_ht
        self.quantite_en_stock = quantite_en_stock

    def __str__(self) -> str:
        """Chaîne décrivant l'article.

        Returns
        -------
        str
            Description de l'article

        Examples
        --------
        >>> article1 = Article(123, "pomme", 0.40, 12)
        >>> print(article1)
        #123: "pomme", 0.40€ H.T.
        """
        return f'#{self.reference}: "{self.intitule}", {self.prix_ht:.2f}€ H.T.'

    def __eq__(self, other: Any) -> bool:
        """Test d'égalité entre deux articles.

        Parameters
        ----------
        other
            Autre objet à comparer

        Returns
        -------
        bool
            True si ce sont les même articles

        Examples
        --------
        >>> article1 = Article(123, "pomme", 0.40, 12)
        >>> article2 = Article(126, "poire", 0.30, 9)
        >>> article3 = Article(123, "pomme", 0.45, 6)
        >>> article1 == article2
        False
        >>> article1 == article3
        True
        """
        if isinstance(other, Article):
            return self.reference == other.reference
        return NotImplemented

    def __lt__(self, other: Any) -> bool:
        """Comparaison de stock.

        Parameters
        ----------
        other
            Autre objet à comparer

        Returns
        -------
        bool
            True si le stock courant est strictement inférieur

        Examples
        --------
        >>> article1 = Article(123, "pomme", 0.40, 12)
        >>> article2 = Article(126, "poire", 0.30, 9)
        >>> article2 < article1
        True
        """
        if isinstance(other, Article):
            return self.quantite_en_stock < other.quantite_en_stock
        return NotImplemented

    def approvisionner(self, nombre_unites: int) -> None:
        """Augmente le stock de l'article.

        Parameters
        ----------
        nombre_unites : int
            la quantité à ajouter

        Examples
        --------
        >>> article = Article(123, "pomme", 0.40, 12)
        >>> article.approvisionner(2)
        >>> article.quantite_en_stock
        14
        """
        self.quantite_en_stock += nombre_unites

    def vendre(self, nombre_unites: int) -> None:
        """Sort des produits du stock.

        Parameters
        ----------
        nombre_unites : int
            la quantité à sortir (vendue)

        Examples
        --------
        >>> article = Article(123, "pomme", 0.40, 12)
        >>> article.vendre(4)
        >>> article.quantite_en_stock
        8
        >>> article.vendre(8)
        >>> article.quantite_en_stock
        0
        """
        if not (isinstance(nombre_unites, int) and (nombre_unites <= self.quantite_en_stock)):
            raise ValueError("Le nombre d'unités doit être un entier inférieur ou égal à la quantité en stock.")
        self.quantite_en_stock -= nombre_unites

    def prix_ttc(self) -> float:
        """Calcul le prix TTC.

        Returns
        -------
        float
            le prix TTC

        Examples
        --------
        >>> article = Article(123, "pomme", 0.40, 12)
        >>> article.prix_ttc()
        0.48
        """
        return round(self.prix_ht * 1.2, 2)
