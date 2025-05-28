
from random import randint
from Plateformes import Plateforme


class Decor:

    def __init__(self, taille_carte_x, taille_carte_y, taille_quadrillage = 50):
        self.plateformes = []
        self.objets = []
        self.taille_carte_x = taille_carte_x
        self.taille_carte_y = taille_carte_y
        self.taille_quadrillage = taille_quadrillage


    def __str__(self):
        print("à coder")


    def ajouter_plateforme(self,plateforme):
        """
        méthode qui ajoute une plateforme (en paramètre) au décor du jeu
        """
        self.plateformes.append(plateforme)



    def ajouter_objet(self,objet):
        """
        méthode qui ajoute un objet (en paramètre) au décor du jeu
        """
        self.objets.append(objet)



    def creer_plateforme_hasard(self, n, hauteur, case):
        """
        méthode qui créé n plateformes à une position aléatoire alignées sur une même hauteur
        elle prend en compte la taille case du quadrillage
        utilisée dans la méthode creer_decor_hasard
        """
        for i in range(1, n+1):
            # On découpe la largeur de l'écran en autant d'intervalles que de plateformes
            intervalle = (int((self.taille_carte_x * (i-1) /n) / case) , int(((self.taille_carte_x * i /n)- 4*case) / 25))
            placement_x = randint(intervalle[0], intervalle[1])
            brique = Plateforme(x_pos= placement_x * case, y_pos= hauteur, x_taille= 4*case, y_taille = case)
            self.ajouter_plateforme(brique)
            print(f"plateforme placée en {placement_x}, {hauteur}")




    def creer_decor_hasard(self):
        """
        méthode qui créé un décor généré aléatoirement en appelant d'autres fonctions dédiées jusqu'à remplir la carte.
        """
        # On place une large plateforme sur tout le bas de la carte
        case = self.taille_quadrillage
        sol = Plateforme(x_pos= 0,y_pos= self.taille_carte_y-case, x_taille= self.taille_carte_x, y_taille= case)
        self.ajouter_plateforme(sol)

        # A intervalle d'espace régulier, on ajoute entre 1 et 3 plateformes alignées
        hauteur = self.taille_carte_y - 7 * case
        while hauteur > 100:
            nb_plateformes = randint(2, 5)
            self.creer_plateforme_hasard(nb_plateformes, hauteur, case)
            hauteur -= 6 * case