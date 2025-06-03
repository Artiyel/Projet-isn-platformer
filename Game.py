from Controleur_Fenetre import ControlleurFenetre
from Controleur_Jeu import ControleurJeu
from StartControler import StartControler
from Controleur_Jeu import ControleurJeu

class Game :

    def __init__(self, dict_entites, buttons, window):
        ''''''
        self.startcontroler = StartControler(self, buttons, window)
        self.controleurjeu = ControleurJeu(dict_entites["decor"].plateformes, dict_entites["player"], dict_entites["entites"], self)
        self.controleurfenetre = ControlleurFenetre(dict_entites["decor"], dict_entites["entites"], dict_entites["player"], self, window)

    def game_start(self):
        self.startcontroler.start()