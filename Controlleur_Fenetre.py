from Decor import Decor
from FenetreJeu import FenetreJeu

class ControlleurFenetre:
    """
    Classe qui gère la fenêtre de jeu.
    """
    def __init__(self, decor: Decor):
        self.fenetre = FenetreJeu(decor)
        self.running = True

    def run(self):
        """
        Lance la boucle principale de la fenêtre.
        """
        while self.running:
            self.fenetre.update()
            for event in self.fenetre.get_events():
                if event.type == self.fenetre.QUIT:
                    self.running = False