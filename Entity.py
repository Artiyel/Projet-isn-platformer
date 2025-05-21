import pygame
import time as time
import numpy as np


pygame.init()

class Entity:
    def __init__(self):
        self.x = 0  # position horizontale de l'entité
        self.y = 0  # position verticale de l'entité
        self.masse = 50
        self.vel = np.array([0, 0]) # vitesse de l'entité (vecteur 2D)
        self.vie = 100  # points de vie de l'entité
        self.invincibility = False


    def gravite(self):
        '''applique la gravité à l'entité'''
        # on modifie la vitesse verticale de l'entité
        self.vel = self.vel + np.array(0, 9.81 * self.masse)  # ajout de l'accélération due à la gravité à la vitesse verticale (car ici, on a un /_\t fixe)


    def sauter(self):
        """
        méthode permettant d'initier un saut d'une entité
        """
        self.vel[1] -= 200



class Player(Entity):
    def __init__(self):
        super.__init__()

     

class Ennemy(Entity):
    def __init__(self):
        super.__init__()
