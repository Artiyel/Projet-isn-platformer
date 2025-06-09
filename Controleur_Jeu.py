from Decor import Decor
import numpy as np
from Entity import Entity
import pygame
from Graphe import Graphe
import heapq

pygame.init()

class ControleurJeu:

    def __init__(self, decor, perso, entites, jeu):
        self.jeu = jeu
        self.decor = decor.plateformes
        self.perso = perso
        # Prend le premier fantome de la liste s'il existe, sinon None
        self.fantome = entites[0] if entites else None
        self.matrice = decor.quadrillage()
        self.taille_case = decor.taille_quadrillage
        self.graphe = Graphe(self)


    def souhait_action_joueur(self, saut_av, right_av, left_av, events):
        '''
        Gère les actions du joueur en fonction des événements clavier et de l'état des touches.
        - Les touches droite/gauche sont gérées en continu (appui prolongé).
        - La touche saut (haut) est gérée à l'appui.
        '''
        saut = saut_av  # On garde l'état précédent du saut
        right = False   # On réinitialise right/left à chaque frame (car on va tester l'état du clavier)
        left = False

        # gestion des événements pour le saut (action ponctuelle)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    saut = True  # On active le saut à l'appui
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    saut = False  # On désactive le saut au relâchement

        # gestion des touches maintenues pour droite/gauche (déplacement continu)
        keys = pygame.key.get_pressed()  # Récupère l'état de toutes les touches du clavier
        mvt = self.perso.vitesse_marche  # Vitesse de déplacement

        if keys[pygame.K_RIGHT]:
            self.perso.potentiel_pos_x = self.perso.x + mvt
            right = True  # Si la touche droite est maintenue, on active le déplacement à droite
        if keys[pygame.K_LEFT]:
            self.perso.potentiel_pos_x = self.perso.x - mvt
            left = True   # Si la touche gauche est maintenue, on active le déplacement à gauche

        # On retourne les états pour la frame suivante
        return saut, right, left
    
    def souhait_action_fantome(self,droite,gauche):
        mvt = self.fantome.vitesse_marche
        droite_res, gauche_res = False, False
        print("humm")
        if droite:
            self.fantome.potentiel_pos_x = self.fantome.x + mvt
            droite_res = True
        if gauche:
            print("ok")
            self.fantome.potentiel_pos_x = self.fantome.x - mvt
            gauche_res = True
        return droite_res,gauche_res

    def test_contact_plateforme(self,perso):
        """
        Teste si le personnage est en contact avec une plateforme, ou si sa position rentre en conflit avec une plateforme.
        :return: True si le personnage est en contact avec une plateforme, False sinon
        """
        contact = False
        meilleur_y = None
        for element in self.decor:  # On parcourt les plateformes du décor
            x_min, y_min, x_max, y_max = element.get_min_max()
            # Test de contact vertical et horizontal
            if (perso.y >= (y_min - perso.y_taille)
                and perso.y <= y_max                           # Condition n°1 : le perso est "dans" une plateforme
                and perso.x < x_max
                and perso.x + perso.x_taille > x_min)\
                or (perso.x < x_max                            # Condition n°2 : le perso risque de passer à travers une plateforme en tombant
                and perso.x + perso.x_taille > x_min
                and perso.y + perso.y_taille < y_min
                and perso.y + perso.y_taille + perso.vel[1] > y_min):
                contact = True
                # On cherche la plateforme la plus haute sous le joueur
                if meilleur_y is None or y_min - perso.y_taille < meilleur_y:
                    meilleur_y = y_min - perso.y_taille

        # On ne modifie potentiel_pos_y que si contact
        if contact and meilleur_y is not None and perso.y != meilleur_y:
            perso.potentiel_pos_y = meilleur_y
        else:
            perso.potentiel_pos_y = perso.y

        return contact


    def test_collision_droite(self,perso):
        """
        méthode permettant de vérifier si une entité Perso est en contact avec une plateforme sur le côté droit de l'écran.
        Renvoie un Booléen correspondant.
        """
        res = False
        for element in self.decor:
            x_min, y_min, x_max, y_max = element.get_min_max()
            if self.perso.y < y_max and perso.y + perso.y_taille > y_min and perso.x < x_max and perso.x + perso.x_taille > x_min:
                res = True
                if perso.x != x_min:
                    perso.pos_potentiel_x = x_min
        return res


    def test_collision_gauche(self,perso):
        """
        méthode permettant de vérifier si une entité Perso est en contact avec une plateforme sur le côté gauche de l'écran.
        Renvoie un Booléen correspondant.
        """
        res = False
        for element in self.decor :
            x_min, y_min, x_max, y_max = element.get_min_max()
            if perso.y < y_max and perso.y + perso.y_taille > y_min and (perso.x + perso.x_taille) > x_min and perso.x <= x_max:
                res = True
                if perso.x != x_max:
                    perso.potentiel_pos_x = x_max

        return res

        

    def calcul_mvt(self, saut, right, left,perso):
            ''' 
            méthode qui effectue tous les tests avec les méthodes faites en haut et renvoie la position finale du joueur
            peut être que y'a pas besoin de renvoie et qu'on peut juste update la position dans l'instance perso directement mais pas sûr que ça marche!
            '''
            # self.souhait_action_joueur(saut,right,left,)
            if self.test_contact_plateforme(perso):
                perso.vel[1] = 0
                perso.y = perso.potentiel_pos_y
                if saut:
                    perso.saut()
            else: 
                perso.gravite()
            perso.y += perso.vel[1]

            if right:
                if self.test_collision_droite(perso):
                    perso.x = perso.potentiel_pos_x #à voir si il faut pas le repositionner sur le bord de la plateforme jsp
                else:
                    perso.x = perso.potentiel_pos_x

            if left:
                if self.test_collision_gauche(perso):
                    perso.x = perso.potentiel_pos_x #à voir si il faut pas le repositionner sur le bord de la plateforme jsp

                else:
                    perso.x = perso.potentiel_pos_x
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
    """
    def calcul_action_fantome(self, fantome, player_x, player_y, obstacles):

        Calcule la prochaine action à effectuer pour le fantôme pour suivre le joueur en évitant les obstacles.
        algorithme Dijstra pour trouver le chemin le plus court vers le joueur.
        :param fantome: l'entité fantôme
        :param player_x: la position x du joueur
        :param player_y: la position y du joueur
        :param obstacles: liste des obstacles sous forme de dictionnaires avec les clés "x", "y", "w", "h"
        :return: None, met à jour l'attribut next_action du fantôme

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

        Applique l'action calculée au fantôme.

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
        fantome.y += fantome.vel[1] * delta_time"""

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
