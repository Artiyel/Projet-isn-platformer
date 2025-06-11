from Controleur_Fenetre import ControlleurFenetre
from Controleur_Jeu import ControleurJeu
from StartControler import StartControler
from Controleur_Jeu import ControleurJeu
from MenuInGame import MenuInGame
from MenuPrincipal import MenuPrincipal
import Entity as e
import Decor as d

class Game :

    def __init__(self, mode, window, taille_carte=(3000, 20000)):
        '''
        Classe principale du jeu, elle initialise les entités et les contrôleurs.
        Entrée :
            window : instance de pygame.display
        '''
        self.dict_entites = dict()
        self.mode = mode

        #On initialise le personnage
        self.player = e.Player()
        self.player.x = 100
        self.player.y = taille_carte[1]
        self.dict_entites["player"] = self.player

        # On initialise le fantome
        if mode == "fantome":
            self.fantome = e.Fantome()
            self.fantome.x = taille_carte[0]-100
            self.fantome.y = taille_carte[1]
            self.dict_entites["entites"] = [self.fantome]
        else:
            self.dict_entites["entites"] = []

        #On créé le decor
        self.decor = d.Decor(taille_carte[0],taille_carte[1])
        self.decor.creer_decor_hasard()
        self.dict_entites["decor"] = self.decor

    def initialize_controlers(self, window):
        '''
        Initialise les contrôleurs du jeu.
        '''
        self.startcontroler = StartControler(self, window)
        self.controleurjeu = ControleurJeu(self.dict_entites, self)
        self.controleurfenetre = ControlleurFenetre(self.dict_entites, self, window)
