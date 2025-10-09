def afficher_titre(texte: str, largeur: int, alignement: str = "centre") -> None:
    """Affiche un ensemble de lignes encadré par des astérisques.

    S'assure que la plus longue ligne tient dans le cadre, et propose 3
    alignements du texte : à gauche (, centré (défaut), ou à droite.

    Parameters
    ----------
    texte : list
        Une liste de chaînes de caractères, chaque élément étant une ligne à afficher.

    largeur : int
        La largeur minimale du cadre à afficher.

    alignement : {'centre', 'gauche', 'droite'}
        Alignement du texte : 'centre' (défaut), 'gauche', ou 'droite'.

    Examples
    --------
    >>> texte = [
    ...    "The Ingenious Gentleman",
    ...    "Don Quixote of La Mancha",
    ...    "",
    ...    "Composed by Miguel de Cervantes",
    ...    "",
    ...    "With printing privilege",
    ...    "in Madrid",
    ...    "in the year of our Lord 1605"
    ... ]
    >>> afficher_titre(texte, 3)
    *********************************
    *    The Ingenious Gentleman    *
    *   Don Quixote of La Mancha    *
    *                               *
    *Composed by Miguel de Cervantes*
    *                               *
    *    With printing privilege    *
    *           in Madrid           *
    * in the year of our Lord 1605  *
    *********************************
    >>> afficher_titre(texte, 40, 'gauche')
    ******************************************
    *The Ingenious Gentleman                 *
    *Don Quixote of La Mancha                *
    *                                        *
    *Composed by Miguel de Cervantes         *
    *                                        *
    *With printing privilege                 *
    *in Madrid                               *
    *in the year of our Lord 1605            *
    ******************************************
    """

    # Calcule la largeur du texte (sans compter l'étoile au début et à la fin)
    largeur_: int = max([largeur] + [len(string) for string in texte])

    # Définis le format pour l'alignement
    format_: str
    if alignement == "gauche":
        format_ = "<"
    elif alignement == "droite":
        format_ = ">"
    else:
        format_ = "^"

    # Calcule la première ligne (qui est identique à la dernière ligne)
    premiere_ligne: list[str] = ["*" * (largeur_ + 2)]

    # Calcule la chaîne de caractères finale
    res: str = "\n".join(premiere_ligne + [f"*{string:{format_}{largeur_}}*" for string in texte] + premiere_ligne)

    # Affiche le résultat
    print(res)
