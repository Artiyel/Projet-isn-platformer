from Decor import Decor
import numpy as np
from Entity import Entity
import pygame


class ControleurJeu:

    def __init__(self, decor, perso, liste_ennemis):
        self.decor = decor
        self.perso = perso

    def test_contact_plateforme(self, entite):
        """
        teste si le personnage est en contact avec une plateforme, ou si sa position rentre en conflit avec une plateforme
        :param entite: l'entité à tester (ici le personnage)
        :return: True si le personnage est en contact avec une plateforme, False sinon
        """
        for element in self.decor.plateformes :
            # On récupère les coordonnées de la plateforme
            x_min, y_min, x_max, y_max = element.get_min_max()
            # On teste si le personnage est en contact avec la plateforme
            if self.perso.y_pos + self.perso.y_taille == y_min and self.perso.x_pos < x_max and self.perso.x_pos + self.perso.x_taille > x_min:
                contact = True
            else:
                contact = False
        return contact


    def test_contact(self): #contact ennemi ???
        print("stuff to do")


    def souhait_action(self):
        '''
        récupère l'action souhaitée par l'utilisateur via le clavier
        '''
        #récupère l'information du déplacement/ de l'action (si jamais on en ajoute) que veut effectuer le joueur
        for event in pygame.event.get():
            mvt = 5 #nombre de pixel que fait bouger un déplacement
            if event.type == pygame.KEYDOWN: #recup l'information du clavier du joueur 
                if event.key == pygame.K_UP:
                    saut = True
                
                else:
                    saut = False

                if event.key == pygame.K_RIGHT:
                    self.perso.potentiel_pos_x = self.perso.x + mvt
                    left = True


                if event.key == pygame.K_LEFT:
                    self.perso.potentiel_pos_x = self.perso.x - mvt
                    right = True
            else:
                right = False
                left = False
            
            if event.type == pygame.KEYUP: #si jamais l'utilisateur a maintenu enfoncé et s'arrête
                if event.key == pygame.K_RIGHT:
                    right = False

                if pygame.key == pygame.K_LEFT:
                    left = False         #à voir comment on communique cette information après 

        return saut, right, left


    def calcul_mvt(self):
        ''' 
        méthode qui effectue tous les tests avec les méthodes faites en haut et renvoie la position finale du joueur
        peut être que y'a pas besoin de renvoie et qu'on peut juste update la position dans l'instance perso directement mais pas sûr que ça marche!'''
        #... y'a masse trucs à rajouter là 
        saut, right, left = self.souhait_action()

        if test_contact_plateforme(self.perso):
            if saut:
                self.perso.saut()
        else: 
            self.perso.gravite()

       
        pos_x = self.perso.potentiel_pos_x
        pos_y = self.perso.potentiel_pos_y
        return pos_x, pos_y #peut être que y'en a pas besoin en vrai