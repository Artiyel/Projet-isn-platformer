from Controleur_Fenetre import ControlleurFenetre
from Controleur_Jeu import ControleurJeu
from StartControler import StartControler
from Controleur_Jeu import ControleurJeu

class Game :

    def __init__(self,dict_entites,buttons):
        """"""
        self.startcontroler = StartControler(self, buttons)
        self.controleurjeu = ControleurJeu(dict_entites["decor"],dict_entites["player"],dict_entites["entites"],self)
        self.controleurfenetre = ControlleurFenetre(dict_entites["decor"],dict_entites["entites"],dict_entites["player"],self)

    def game_start(self):
        self.startcontroler.start()