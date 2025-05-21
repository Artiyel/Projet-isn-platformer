
from random import randint
from Plateformes import Plateforme


class Decor:

    def __init__(self,plateformes, objets, taille_carte_x, taille_carte_y):
        self.plateformes = []
        self.objets = []
        self.taille_carte_x = taille_carte_x
        self.taille_carte_y = taille_carte_y


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



    def creer_plateforme_hasard(self, n, hauteur):
        """
        méthode qui créé n plateformes à une position aléatoire sur une même hauteur
        """
        for i in range(1, n+1):
            # On découpe la largeur de l'écran en autant d'intervalles que de plateformes
            intervalle = (self.taille_carte_x * (i-1) /n , (self.taille_carte_x * i /n)-25)
            placement_x = randint(intervalle[0], intervalle[1])
            brique = Plateforme(x_pos= placement_x, y_pos= hauteur, x_taille= 25, y_taille = 5)
            self.ajouter_plateforme(brique)




    def creer_decor_hasard(self):
        """
        méthode qui créé un décor généré aléatoirement en appelant d'autres fonctions dédiées jusqu'à remplir la carte.
        """
        # On place une large plateforme sur tout le bas de la carte
        sol = Plateforme(x_pos= 0,y_pos= self.taille_carte_y-5, x_taille= self.taille_carte_x, y_taille= 5)
        self.ajouter_plateforme(sol)

        # A intervalle d'espace régulier,
        hauteur = self.taille_carte_y - 100
        while hauteur > 100:
            nb_plateformes = randint(1, 3)
            creer_plateformes_hasard(nb_plateformes, hauteur)




