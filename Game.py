from Controleur_Fenetre import ControlleurFenetre
from Controleur_Jeu import ControleurJeu
from StartControler import StartControler

class Game :

    def __init__(self,dict_entites):
        """"""
        self.startcontroler = StartControler(self)
        self.controleurjeu = ControleurJeu(self,dict_entites["decor"],dict_entites["player"],dict_entites["entites"])
        self.controleurfenetre = ControlleurFenetre(self,dict_entites["decor"],dict_entites["entites"],dict_entites["player"])

    def game_start(self):
        self.startcontroler.start()