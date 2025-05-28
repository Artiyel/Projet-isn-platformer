import pygame
import numpy as np


pygame.init()

class Entity:
    def __init__(self):
        self.x = 0  # position horizontale de l'entité
        self.y = 0  # position verticale de l'entité
        self.x_taille = 10
        self.y_taille = 20
        self.masse = 10
        self.vel = [0, 0] # vitesse de l'entité (vecteur 2D)
        self.vie = 100  # points de vie de l'entité
        self.invincibility = False
        self.vitesse_marche = 20 #vitesse de déplacement horizontale


    def get_min_max(self):
        """
        Méthode permettant d'obtenir les coordonnées des limites de l'entité
        """
        return self.x_pos, self.y_pos, self.x_pos + self.x_taille, self.y_pos +self.y_taille


    def placer(self, x, y):
        """
        méthode pour téléporter l'entité à des coordonnées voulues.
        """
        self.x = x
        self.y = y


    def gravite(self):
        """
        applique la gravité à l'entité
        """
        # on modifie la vitesse verticale de l'entité
        self.vel = self.vel[1] + 9.81 * self.masse  # ajout de l'accélération due à la gravité à la vitesse verticale (car ici, on a un /_\t fixe)


    def mouvement_droite(self):
        """
        méthode déplaçant l'entité vers la droite d'une distance égale à l'attribut vitesse_marche de l'entité
        """
        self.x += self.vitesse_marche

    def mouvement_gauche(self):
        """
        méthode déplaçant l'entité vers la gauche d'une distance égale à l'attribut vitesse_marche de l'entité
        """
        self.x -= self.vitesse_marche

    def saut(self):
        """
        méthode faisant sauter l'entité par une impulsion verticale.
        """
        self.vel[1] -= 200


class Player(Entity):
    def __init__(self):
        super().__init__()

     

class Ennemy(Entity):
    def __init__(self):
        super().__init__()
