import pygame
import time as time
import numpy as np


pygame.init()

class Entity:
    def __init__(self):
        self.x = 0  # position horizontale de l'entité
        self.y = 0  # position verticale de l'entité
        self.masse = 50

        self.vel = np.array([0, 0])


    def gravite(self):
        '''applique la gravité à l'entité'''
        # on modifie la vitesse verticale de l'entité
        self.vel[1] += 9.81 * self.masse  # ajout de l'accélération due à la gravité à la vitesse verticale (car ici, on a un /_\t fixe)



class Player(Entity):
    def __init__(self):
        super.__init__()

     

class Ennemy(Entity):
    def __init__(self):
        super.__init__()
