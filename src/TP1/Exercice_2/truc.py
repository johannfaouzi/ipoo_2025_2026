def affiche_titre(texte: list[str], largeur: int) -> None:
    """Affiche les chaînes de caractères données centrées encadrées par des
    `*`

    Parameters
    ----------
    texte : list[str]
        liste des chaines de caractères à afficher
    largeur : int
        largeur du titre (en nombre de charactères)
    """
    m: int = max([largeur] + [len(t) for t in texte])
    barre_horizontale: list[str] = ["*" * (m + 2)]
    texte = ["*" + t.center(m) + "*" for t in texte]
    print("\n".join(barre_horizontale + texte + barre_horizontale))



affiche_titre(["tyqdsfru", "uim"], 15)
