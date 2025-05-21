import pygame
import time as time
import numpy as np


pygame.init()

class Entity:
    ''' 
    classe de base pour les entités du jeu
    (joueur, ennemis, objets) 
    '''
    def __init__(self):
        self.x = 0  # position horizontale de l'entité
        self.y = 0  # position verticale de l'entité
        self.masse = 50
        self.vel = np.array([0, 0]) # vitesse de l'entité (vecteur 2D)
        self.vie = 100  # points de vie de l'entité
        self.invincibility = False



    def gravite(self) :
        """
        Gère la gravité du personnage
        """
        #on regarde si le personnage est sur le sol ou pas, et on applique la gravité en conséquence
        while test_contact_plateforme(self.perso) == False: 
            # on applique la gravité au personnage
            # on modifie la vitesse verticale de l'entité
            self.perso.vel[1] += + np.array(0, 9.81 * self.masse)   # ajout de l'accélération due à la gravité à la vitesse verticale (car ici, on a un /_\t fixe)
            # ici, on considère que le perso peut descendre en dehors de la fenêtre de jeu affichée (il peut régresser)
            # on considère que le point de départ (tout en bas) est sur une plateforme qu'il faudra penser à crééer en début de jeu



class Player(Entity):
    '''
    classe du joueur
    hérite de la classe Entity
    '''
    def __init__(self):
        super.__init__()

     

class Ennemy(Entity):
    '''
    classe des ennemis
    hérite de la classe Entity
    '''
    def __init__(self):
        super.__init__()