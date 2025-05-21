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


class Player(Entity):
    def __init__(self):
        super.__init__()

     

class Ennemy(Entity):
    def __init__(self):
        super.__init__()
