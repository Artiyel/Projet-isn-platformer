from Controleur_Fenetre import ControlleurFenetre
from Controleur_Jeu import ControleurJeu
from StartControler import StartControler
from Controleur_Jeu import ControleurJeu
from MenuInGame import MenuInGame
from MenuPrincipal import MenuPrincipal
import Entity as e
import Decor as d

class Game :

    def __init__(self, window, taille_carte=(3000, 20000)):
        '''
        Classe principale du jeu, elle initialise les entités et les contrôleurs.
        Entrée :
            window : instance de pygame.display
        '''
        self.dict_entites = dict()

        #personnage
        self.player = e.Player()
        self.player.x = 100
        self.player.y = taille_carte[1]
        self.dict_entites["player"] = self.player

        self.fantome = e.Fantome()
        self.fantome.x = taille_carte[0]-100
        self.fantome.y = taille_carte[1]
        self.dict_entites["entites"] = [self.fantome]

        #decor
        self.decor = d.Decor(taille_carte[0],taille_carte[1])
        self.decor.creer_decor_hasard()
        self.dict_entites["decor"] = self.decor


        self.startcontroler = StartControler(self, window)
        self.controleurjeu = ControleurJeu(self.dict_entites, self)
        self.controleurfenetre = ControlleurFenetre(self.dict_entites, self, window)
