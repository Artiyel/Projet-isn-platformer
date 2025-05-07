import pygame
import time as time
import numpy as np


pygame.init()

class Entity:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.masse = 50
        # self.vitesse = (0, 0)
        self.gravity_pixels = self.gravity * 1080 / 0.07
        self.potentiel_pos_y = 0
        self.potentiel_pos_x = 0
        self.vitesse = np.array([0, 0])

    def appliquer_physique(self):
        """
        Méthode qui calcule la vitesse d'une entité à un instant donné
        Prend en compte la gravité et les frottements de l'air, mais pas les déplacements et sauts
        """
        current_time = time.time()
        elapsed_time = current_time - self.last_update_time
        self.last_update_time = current_time  # on réinitialise le moment de la dernière itération
        time_in_s = elapsed_time / 1000  # conversion du temps en secondes

        # On calcule les vitesses de man selon x et y
        self.vitesse[0] -= self.frottement_pixels * self.vitesse[0] / self.masse * time_in_s
        self.vitesse[1] -= self.frottement_pixels * self.vitesse[1] / self.masse * time_in_s - (
                        self.gravity_pixels * time_in_s)

        # On utilise les vitesses et l'intervalle de temps pour mettre les positions du personnage à jour
        self.x += self.vitesse[0] * elapsed_time
        self.y += self.vitesse[1] * elapsed_time
    

    def bouger(self,ajout_x, ajout_y):
        '''recupère une info donnée par le controlleur après avoir fait tous les teste sur de combien il doit bouger et update les variables self.x et self.y'''
        # dépacements
        # on modifie les valeurs des vitesses verticales et horizontales
        self.x += ajout_x
        self.y += ajout_y



class Player(Entity):
    def __init__(self):
        super.__init__()

     

class Ennemy(Entity):
    def __init__(self):
        super.__init__()
