import random

from .domino import Domino


def affiche_dominos(liste: list[Domino]) -> str:
    """Affiche les dominos dans la liste.

    Parameters
    ----------
    liste : list[Domino]
        Liste de dominos.

    Returns
    -------
    str
        Chaîne de caractères représentant la liste de dominos.

    Examples
    --------
    >>> affiche_dominos([Domino(2, 6), Domino(4, 3)])
    '[2|6] - [4|3]'
    """
    return " - ".join(str(domino) for domino in liste)


def cree_jeu_dominos() -> list[Domino]:
    """Crée le jeu de dominos.

    Returns
    -------
    list[Domino]
        Le jeu comprenant tous les dominos.

    Examples
    --------
    >>> liste = cree_jeu_dominos()
    >>> isinstance(liste, list)
    True
    >>> len(liste)
    28
    >>> print(affiche_dominos(liste))
    [0|0] - [1|0] - [1|1] - [2|0] - [2|1] ...
    """
    return [Domino(i, j) for i in range(7) for j in range(i + 1)]


def choisit_alea(liste: list[Domino]) -> Domino:
    """Tire au hasard un domino et le renvoie.

    Parameters
    ----------
    liste : list[Domino]
        Liste de dominos.

    Returns
    -------
    Domino
        Le domino tiré au hasard.

    Examples
    --------
    >>> print(choisit_alea([Domino(2, 6)]))
    [2|6]
    """
    return liste.pop(random.randrange(len(liste)))


def bon_jeu(main: list[Domino], dominos_poses: list[Domino]) -> bool:
    """Détermine si au moins un domino de la main peut être posé.

    Parameters
    ----------
    main : list[Domino]
        Liste des dominos dans la main.

    dominos_poses : list[Domino]
        Liste des dominos posés.

    Returns
    -------
    bool
        Vrai s'il est possible de poser au moins un domino de la main,
        faux sinon.

    Examples
    --------
    >>> bon_jeu([Domino(0, 1)], [])
    True
    >>> dominos_poses = [Domino(2, 5), Domino(3, 4)]
    >>> bon_jeu([Domino(0, 1)], dominos_poses)
    False
    >>> bon_jeu([Domino(2, 0)], dominos_poses)
    False
    >>> bon_jeu([Domino(0, 4)], dominos_poses)
    True
    """
    if len(dominos_poses) == 0:
        return True
    for domino in main:
        if dominos_poses[-1].extr_B in (domino.extr_A, domino.extr_B):
            return True
    return False


def choix_joueur(main: list[Domino], dominos_poses: list[Domino]) -> int:
    """Permet au joueur de choisir un domino dans sa main pour le poser.

    Parameters
    ----------
    main : list[Domino]
        Liste des dominos dans la main.

    dominos_poses : list[Domino]
        Liste des dominos posés.

    Returns
    -------
    idx : int
        L'indice du domino de la main à jouer, ou -1 pour arrêter.
    """
    print("Main actuelle :", affiche_dominos(main))
    string: str = f"Indiquez l'indice du domino souhaité " f"(de 0 à {len(main) - 1}, -1 pour quitter) : "

    while True:
        idx = int(input(string))
        choix_valide = (
            # Pour quitter la partie
            (idx == -1)
            or (
                # Domino présent dans la main
                idx in range(len(main))
                and
                # Domino posable
                (len(dominos_poses) == 0)
                or ((len(dominos_poses) > 0) and dominos_poses[-1].accepte_apres(main[idx]))
            )
        )
        if not choix_valide:
            print("Choix non valide.")
        else:
            break

    return idx


def jouer() -> None:
    """Joue une partie de dominos."""

    # Initialisation du jeu
    jeu: list[Domino] = cree_jeu_dominos()

    # Tirage de la main initiale (6 dominos)
    main: list[Domino] = []
    for _ in range(6):
        main.append(choisit_alea(jeu))

    # Liste des dominos poses
    dominos_poses: list[Domino] = []

    # Initialisation de l'indice du domino choisi par le joueur
    choix: int = 0

    # Définition des critères d'arrêt du jeu
    def criteres(jeu: list[Domino], main: list[Domino], dominos_poses: list[Domino], choix: int) -> bool:
        return (len(main) == 0) or ((len(jeu) == 0) and not bon_jeu(main, dominos_poses)) or (choix == -1)

    # Tant qu'un aucun critère d'arrêt n'est vérifié
    while not criteres(jeu, main, dominos_poses, choix):
        # Si le joueur peut poser un domino
        if bon_jeu(main, dominos_poses):
            # Lui demander quel domino posé
            print("Les dominos posés sont :", affiche_dominos(dominos_poses))
            choix = choix_joueur(main, dominos_poses)
            if choix != -1:
                domino_pose = main.pop(choix)
                if (len(dominos_poses) == 0) or (domino_pose.extr_A == dominos_poses[-1].extr_B):
                    dominos_poses.append(domino_pose)
                else:
                    dominos_poses.append(domino_pose.retourne())

        # Sinon
        else:
            # Tirer un domino dans le jeu
            domino = choisit_alea(jeu)
            main.append(domino)
            print(f"Tirage d'un domino dans le jeu : {domino}")

        print()

    # Affichage du critère d'arrêt
    if choix == -1:
        print("Vous avez décidé d'arrêter le jeu.")
    elif len(main) == 0:
        print("Vous avez gagné.")
    elif (len(jeu) == 0) and not bon_jeu(main, dominos_poses):
        print("Vous avez perdu.")
