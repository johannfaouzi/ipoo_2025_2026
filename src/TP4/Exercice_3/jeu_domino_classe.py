import random

from .domino import Domino


class JeuDomino:
    """Implémente un jeu de domino, interactif."""

    def __init__(self) -> None:
        """Créé une nouvelle partie de domino

        Implémentation de la fonction cree_jeu_dominos() de la partie II.

        """
        self.__jeu: list[Domino] = [Domino(i, j) for i in range(7) for j in range(i + 1)]
        self.__main: list[Domino] = []
        for _ in range(6):
            self.__choisit_alea()
        self.__dominos_poses: list[Domino] = []

    @staticmethod
    def __str_dominos(liste: list[Domino]) -> str:
        """Affiche les dominos dans la liste."""
        return " - ".join(str(domino) for domino in liste)

    def affiche_dominos_poses(self) -> None:
        """Affiche les dominos joués jusqu'ici."""
        print("Les dominos posés sont :", self.__class__.__str_dominos(self.__dominos_poses))

    def affiche_main(self) -> None:
        """Affiche la main du joueur."""
        print("Main actuelle :", self.__class__.__str_dominos(self.__main))

    def __choisit_alea(self, verbose: bool = False) -> Domino:
        """Choisi un domino aléatoirement dans la pioche et l'ajoute à la main.

        Parameters
        ----------
        verbose : bool
            Si vrai, affiche le domino tiré.

        """
        domino: Domino = self.__jeu.pop(random.randrange(len(self.__jeu)))
        self.__main.append(domino)
        if verbose:
            print(f"Tirage d'un domino dans le jeu : {domino}")
        return domino

    def bon_jeu(self) -> bool:
        """Vérifie que le joueur peut jouer un domino de sa main.

        Returns
        -------
        bool
            True si le jeu peut continuer.

        Examples
        --------
        """
        if len(self.__dominos_poses) == 0:
            return True
        for domino in self.__main:
            if self.__dominos_poses[-1].extr_B in (domino.extr_A, domino.extr_B):
                return True
        return False

    def choix_joueur(self) -> int:
        """Demande au joueur quel domino jouer.

        Returns
        -------
        int
            L'indice du domino de la main à jouer, ou -1 pour arrêter.
        """
        string: str = f"Indiquez l'indice du domino souhaité " f"(de 0 à {len(self.__main) - 1}, -1 pour quitter) : "

        critere: bool = True
        while critere:
            idx: int = int(input(string))
            choix_valide: bool = (
                # Pour quitter la partie
                (idx == -1)
                or (
                    # Domino présent dans la main
                    idx in range(len(self.__main))
                    and
                    # Domino posable
                    (len(self.__dominos_poses) == 0)
                    or ((len(self.__dominos_poses) > 0) and self.__dominos_poses[-1].accepte_apres(self.__main[idx]))
                )
            )
            if not choix_valide:
                print("Choix non valide.")
            else:
                break
        return idx

    def criteres(self, choix: int) -> bool:
        """Définis les critères d'arrêt du jeu.

        Parameters
        ----------
        choix : int
            L'indice du domino choisi par le joueur.

        Returns
        -------
        bool
            Vrai si le jeu s'arrête, faux sinon.

        """
        return (len(self.__main) == 0) or ((len(self.__jeu) == 0) and not self.bon_jeu()) or choix == -1

    def jouer(self) -> None:
        """Lance la partie."""
        # Initialisation de l'indice du domino choisi par le joueur
        choix = 0

        # Tant qu'un aucun critère d'arrêt n'est vérifié
        while not self.criteres(choix):
            # Si le joueur peut poser un domino
            if self.bon_jeu():
                # Lui demander quel domino posé
                self.affiche_dominos_poses()
                self.affiche_main()
                choix = self.choix_joueur()
                if choix != -1:
                    domino_pose = self.__main.pop(choix)
                    if (len(self.__dominos_poses) == 0) or (domino_pose.extr_A == self.__dominos_poses[-1].extr_B):
                        self.__dominos_poses.append(domino_pose)
                    else:
                        self.__dominos_poses.append(domino_pose.retourne())

            # Sinon
            else:
                # Tirer un domino dans le jeu
                self.__choisit_alea(True)

            print()

        # Affichage du critère d'arrêt
        if choix == -1:
            print("Vous avez décidé d'arrêter le jeu.")
        elif len(self.__main) == 0:
            print("Vous avez gagné.")
        elif (len(self.__jeu) == 0) and not self.bon_jeu():
            print("Vous avez perdu.")
