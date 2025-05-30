from Decor import Decor
import numpy as np
from Entity import Entity
import pygame
import heapq

pygame.init()

class ControleurJeu:

    def __init__(self, decor, perso,fantome, jeu):
        self.jeu = jeu
        self.decor = decor
        self.perso = perso
        self.fantome = fantome


    def souhait_action_joueur(self, saut_av, right_av, left_av):
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
            peut être que y'a pas besoin de renvoie et qu'on peut juste update la position dans l'instance perso directement mais pas sûr que ça marche!
            '''
            self.souhait_action_joueur(saut,right,left)

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

    def detecte_collision(self, entite, x, y, obstacles):
        """
        Vérifie si l'entité placée en (x, y) entre en collision avec un des obstacles.
        :param entite: l'entité à tester
        :param x: position x de l'entité
        :param y: position y de l'entité
        :param obstacles: liste des obstacles sous forme de dictionnaires avec les clés "x", "y", "w", "h"
        :return: True si une collision est détectée, False sinon
        """
        for obs in obstacles:
            ox, oy, ow, oh = obs["x"], obs["y"], obs["w"], obs["h"]
            if (x + entite.x_taille > ox and x < ox + ow and
                y + entite.y_taille > oy and y < oy + oh):
                return True
        return False

    def calcul_action_fantome(self, fantome, player_x, player_y, obstacles):
        """
        Calcule la prochaine action à effectuer pour le fantôme pour suivre le joueur en évitant les obstacles.
        algorithme Dijstra pour trouver le chemin le plus court vers le joueur.
        :param fantome: l'entité fantôme
        :param player_x: la position x du joueur
        :param player_y: la position y du joueur
        :param obstacles: liste des obstacles sous forme de dictionnaires avec les clés "x", "y", "w", "h"
        :return: None, met à jour l'attribut next_action du fantôme
        """
        actions = ["droite", "gauche", "saut"]
        heap = []
        visited = set()
        heapq.heappush(heap, (0, fantome.x, fantome.y, fantome.vel[1], []))

        while heap:
            cost, x, y, vel_y, chemin = heapq.heappop(heap)
            if abs(x - player_x) < 5 and abs(y - player_y) < 5:
                fantome.next_action = chemin[0] if chemin else None
                return

            state = (round(x, 1), round(y, 1), round(vel_y, 1))
            if state in visited:
                continue
            visited.add(state)

            for action in actions:
                nx, ny, nvel_y = x, y, vel_y
                if action == "droite":
                    nx += fantome.vitesse * 0.1
                elif action == "gauche":
                    nx -= fantome.vitesse * 0.1
                elif action == "saut":
                    nvel_y = -200

                nvel_y += 9.81 * fantome.masse * 0.1
                ny += nvel_y * 0.1

                if ny < 0:
                    ny = 0
                    nvel_y = 0

                if self.detecte_collision(fantome, nx, ny, obstacles):
                    continue

                heapq.heappush(heap, (cost + 1, nx, ny, nvel_y, chemin + [action]))

        fantome.next_action = None

    def appliquer_action_fantome(self, fantome, delta_time):
        """
        Applique l'action calculée au fantôme.
        """
        if fantome.next_action == "droite":
            fantome.x += fantome.vitesse * delta_time
            fantome.direction = np.array([1, 0])
        elif fantome.next_action == "gauche":
            fantome.x -= fantome.vitesse * delta_time
            fantome.direction = np.array([-1, 0])
        elif fantome.next_action == "saut":
            fantome.vel[1] = -200
            fantome.direction = np.array([0, -1])
        # Gravité
        fantome.vel[1] += 9.81 * fantome.masse * delta_time
        fantome.y += fantome.vel[1] * delta_time

    def __str__(self):
        info = "=== ControleurJeu ===\n"
        info += f"Décor : {self.decor}\n"
        info += f"Joueur : x={self.perso.x}, y={self.perso.y}\n"
        if self.fantome is not None:
            en_contact = self.fantome.est_en_contact(self.perso.x, self.perso.y)
            info += (
                f"Fantome : x={self.fantome.x}, y={self.fantome.y}, "
                f"next_action={self.fantome.next_action}, "
                f"en_contact={'Oui' if en_contact else 'Non'}\n"
            )
        else:
            info += "Fantome : Aucun\n"
        return info

if __name__ == "main":
    print('bah rien ducoup')
