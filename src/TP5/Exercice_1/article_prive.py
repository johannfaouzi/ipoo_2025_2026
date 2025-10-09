from typing import Any


class ArticlePrive:
    """Article d'un supermarche.

    Parameters
    ----------
    reference : int
        reference de l'article

    intitule : str
        intitule de l'article

    prix_ht : float
        prix hors taxes

    quantite_en_stock : int
        quantite en stock de l'article

    Examples
    --------
    >>> article1 = ArticlePrive(123, "pomme", 0.40, 12)
    >>> article2 = ArticlePrive(126, "poire", 0.30, 8)
    >>> article1 == article2
    False
    >>> article2 < article1
    True
    >>> article2.approvisionner(8)
    >>> article1 < article2
    True
    >>> article2.vendre(20)
    False
    >>> article2.vendre(6)
    True
    >>> article2 < article1
    True
    """

    def __init__(self, reference: int, intitule: str, prix_ht: float, quantite_en_stock: int) -> None:
        self.__reference = reference
        self.__intitule = intitule
        self.__prix_ht = prix_ht
        self.__quantite_en_stock = quantite_en_stock

    def __str__(self) -> str:
        """Chaîne decrivant l'article.

        Returns
        -------
        str
            description de l'article

        Examples
        --------
        >>> article1 = ArticlePrive(123, "pomme", 0.40, 12)
        >>> print(article1)
        #123: "pomme", 0.40€ H.T.
        """
        return f'#{self.__reference}: "{self.__intitule}", {self.__prix_ht:.2f}€ H.T.'

    def __eq__(self, other: Any) -> bool:
        """Test d'egalite entre deux articles.

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
        >>> article1 = ArticlePrive(123, "pomme", 0.40, 12)
        >>> article2 = ArticlePrive(126, "poire", 0.30, 9)
        >>> article3 = ArticlePrive(123, "pomme", 0.45, 6)
        >>> article1 == article2
        False
        >>> article1 == article3
        True
        """
        if isinstance(other, ArticlePrive):
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
            True si le stock courant est strictement inferieur

        Examples
        --------
        >>> article1 = ArticlePrive(123, "pomme", 0.40, 12)
        >>> article2 = ArticlePrive(126, "poire", 0.30, 9)
        >>> article2 < article1
        True
        """
        if isinstance(other, ArticlePrive):
            return self.quantite_en_stock < other.quantite_en_stock
        return NotImplemented

    def approvisionner(self, nombre_unites: int) -> None:
        """Augmente le stock de l'article.

        Parameters
        ----------
        nombre_unites : int
            la quantite à ajouter

        Examples
        --------
        >>> article = ArticlePrive(123, "pomme", 0.40, 12)
        >>> article.approvisionner(2)
        >>> article.quantite_en_stock
        14
        """
        self.__quantite_en_stock += nombre_unites

    def vendre(self, nombre_unites: int) -> bool:
        """Sort des produits du stock.

        Parameters
        ----------
        nombre_unites : int
            la quantite à sortir (vendue)

        Returns
        -------
        bool
            True si la vente a reussi (stock suffisant)

        Examples
        --------
        >>> article = ArticlePrive(123, "pomme", 0.40, 12)
        >>> article.vendre(20)
        False
        >>> article.vendre(8)
        True
        >>> article.quantite_en_stock
        4
        """
        if nombre_unites > self.__quantite_en_stock:
            return False
        self.__quantite_en_stock -= nombre_unites
        return True

    def prix_ttc(self) -> float:
        """Calcul le prix TTC.

        Returns
        -------
        float
            le prix TTC

        Examples
        --------
        >>> article = ArticlePrive(123, "pomme", 0.40, 12)
        >>> article.prix_ttc()
        0.48
        """
        return round(self.__prix_ht * 1.2, 2)

    @property
    def reference(self) -> int:
        return self.__reference

    @property
    def intitule(self) -> str:
        return self.__intitule

    @property
    def prix_ht(self) -> float:
        return self.__prix_ht

    @property
    def quantite_en_stock(self) -> int:
        return self.__quantite_en_stock
