from Decor import Decor
import numpy as np
from Entity import Entity
import pygame

pygame.init()

class ControleurJeu:

    def __init__(self, decor, perso, liste_ennemis,jeu):
        self.jeu = jeu
        self.decor = decor
        self.perso = perso


    def souhait_action(self, saut_av, right_av, left_av):
        '''
        récupère l'action souhaitée par l'utilisateur via le clavier
        '''
        #récupère l'information du déplacement/ de l'action (si jamais on en ajoute) que veut effectuer le joueur
        saut = saut_av
        right = right_av
        left = left_av 
        for event in pygame.event.get():
            print(".")
            mvt = 5 #nombre de pixel que fait bouger un déplacement
            if event.type == pygame.QUIT:
                self.jeu.controleurfenetre.running = False

            if event.type == pygame.KEYDOWN:
                print("OMG")
                print(event.type)
                key = pygame.key.get_pressed()
                if key[pygame.K_UP]:
                    #recup l'information du clavier du joueur 
                    saut = True
                
                else:
                    saut = False

                if key[pygame.K_RIGHT]:
                    self.perso.potentiel_pos_x = self.perso.x + mvt
                    left = True
                    print("A GAUCHE")

                if key[pygame.K_LEFT]:
                    self.perso.potentiel_pos_x = self.perso.x - mvt
                    right = True
                    print("a dro*te")
            else:
                right = False
                left = False
            
            if event.type == pygame.KEYUP: #si jamais l'utilisateur a maintenu enfoncé et s'arrête
                right = False
                left = False         #à voir comment on communique cette information après 

        return saut, right, left


    def test_contact_plateforme(self):
        """
        teste si le personnage est en contact avec une plateforme, ou si sa position rentre en conflit avec une plateforme
        :param entite: l'entité à tester (ici le personnage)
        :return: True si le personnage est en contact avec une plateforme, False sinon
        """
        for element in self.decor.plateformes :
            self.perso.potentiel_pos_y = self.perso.y

            # On récupère les coordonnées de la plateforme
            x_min, y_min, x_max, y_max = element.get_min_max()

            # On teste si le personnage est en contact avec la plateforme
            if self.perso.y >= (y_min - self.perso.y_taille) and self.perso.y <= y_max and self.perso.x < x_max and self.perso.x + self.perso.x_taille > x_min:
                contact = True
                if self.perso.y != y_min - self.perso.y_taille:
                    self.perso.potentiel_pos_y = y_min - self.perso.y_taille

            else:
                contact = False
        return contact


    def test_collision_droite(self):
        """
        méthode permettant de vérifier si une entité Perso est en contact avec une plateforme sur le côté droit de l'écran.
        Renvoie un Booléen correspondant.
        """
        res = False
        for element in self.decor.plateformes:
            x_min, y_min, x_max, y_max = element.get_min_max()
            if self.perso.y < y_max and self.perso.y + self.perso.y_taille > y_min and self.perso.x < x_max and self.perso.x + self.perso.x_taille > x_min:
                res = True
                if self.perso.x != x_min:
                    self.perso.pos_potentiel_x = x_min
        return res


    def test_collision_gauche(self):
        """
        méthode permettant de vérifier si une entité Perso est en contact avec une plateforme sur le côté gauche de l'écran.
        Renvoie un Booléen correspondant.
        """
        res = False
        for element in self.decor.plateformes :
            x_min, y_min, x_max, y_max = element.get_min_max()
            if self.perso.y < y_max and self.perso.y + self.perso.y_taille > y_min and (self.perso.x + self.perso.x_taille) > x_min and self.perso.x <= x_max:
                res = True
                if self.perso.x != x_max:
                    self.perso.potentiel_pos_x = x_max

        return res

        

    def calcul_mvt(self, saut, right, left):
            ''' 
            méthode qui effectue tous les tests avec les méthodes faites en haut et renvoie la position finale du joueur
            peut être que y'a pas besoin de renvoie et qu'on peut juste update la position dans l'instance perso directement mais pas sûr que ça marche!'''
            self.souhait_action(saut,right,left)

            if self.test_contact_plateforme():
                self.perso.y = self.perso.potentiel_pos_y
                if saut:
                    self.perso.saut()
            else: 
                self.perso.gravite()

            if right:
                if self.test_collision_droite():
                    self.perso.x = self.perso.potentiel_pos_x #à voir si il faut pas le repositionner sur le bord de la plateforme jsp
                else:
                    self.perso.x = self.perso.potentiel_pos_x

            if left:
                if self.test_collision_gauche():
                    self.perso.x = self.perso.potentiel_pos_x #à voir si il faut pas le repositionner sur le bord de la plateforme jsp

                else:
                    self.perso.x = self.perso.potentiel_pos_x
                     #same pour ces lignes jsp trop 
                        #peut être que y'en a pas besoin en vrai

if __name__ == "main":
    print('bah rien ducoup')
        