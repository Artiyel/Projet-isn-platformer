import pygame
import numpy as np
import heapq


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
        self.invincibilite = False
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
        self.vel[1] = self.vel[1] + 4  # ajout de l'accélération due à la gravité à la vitesse verticale (car ici, on a un /_\t fixe)


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
        self.vel[1] -= 65

    def __str__(self):
        return (
            f"Entity(x={self.x}, y={self.y}, taille=({self.x_taille},{self.y_taille}), "
            f"vie={self.vie}, vitesse=({self.vel[0]},{self.vel[1]}))"
        )

class Player(Entity):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"Player({super().__str__()})"

class Ennemy(Entity):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"Ennemy({super().__str__()})"


class Fantome(Player):
    def __init__(self):
        super().__init__()
        self.vitesse = 100
        self.direction = np.array([1, 0])
        self.x_taille = 5
        self.y_taille = 5
        self.next_action = None

    def est_en_contact(self, player_x, player_y, marge=5):
        return abs(self.x - player_x) < marge and abs(self.y - player_y) < marge

    def collision(self, x, y, obstacles):
        for obs in obstacles:
            ox, oy, ow, oh = obs["x"], obs["y"], obs["w"], obs["h"]
            if (x + self.x_taille > ox and x < ox + ow and
                y + self.y_taille > oy and y < oy + oh):
                return True
        return False

    def __str__(self):
        return (
            f"Fantome(x={self.x}, y={self.y}, taille=({self.x_taille},{self.y_taille}), "
            f"vitesse={self.vitesse}, direction={self.direction.tolist()}, "
            f"next_action={self.next_action})"
        )