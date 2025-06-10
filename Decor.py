
from random import randint
from Plateformes import Plateforme


class Decor:

    def __init__(self, taille_carte_x, taille_carte_y, taille_quadrillage = 50):
        self.plateformes = []
        self.objets = []
        self.taille_carte_x = taille_carte_x
        self.taille_carte_y = taille_carte_y
        self.taille_quadrillage = taille_quadrillage
        self.arrivee = False


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
            intervalle = (int((self.taille_carte_x * (i-1) /n) / case) , int(((self.taille_carte_x * i /n)- 4*case) / case))
            placement_x = randint(intervalle[0], intervalle[1])
            brique = Plateforme(x_pos= placement_x * case, y_pos= hauteur, x_taille= 4*case, y_taille = case)
            self.ajouter_plateforme(brique)
            print(f"plateforme placée en {placement_x}, {hauteur}")




    def creer_decor_hasard(self):
        """
        méthode qui créé un décor généré aléatoirement en appelant une autre fonction dédiée jusqu'à remplir la carte.
        """
        # On place une large plateforme sur tout le bas de la carte
        case = self.taille_quadrillage
        sol = Plateforme(x_pos= 0,y_pos= self.taille_carte_y-case, x_taille= self.taille_carte_x, y_taille= case)
        self.ajouter_plateforme(sol)

        # A intervalle d'espace régulier, on ajoute entre 1 et 3 plateformes alignées
        hauteur = self.taille_carte_y - 7 * case
        while hauteur > 100:
            nb_plateformes = randint(4, 7)
            self.creer_plateforme_hasard(nb_plateformes, hauteur, case)
            hauteur -= 6 * case
        # On choisit une plateforme aléatoire sur la dernière hauteur comme point d'arrivée
        arrivee = len(self.plateformes) -1
        self.plateformes[arrivee].arrivee = True


    def quadrillage(self):
        """
        méthode qui renvoie une matrice du décor quadrillé, et dont chaque coefficient est 0 si la case est libre et 1 si la case est occupée par une plateforme
        La taille des cases est déterminée par l'attribut taille_quadrillage
        Précision : le point (0,0) de la matrice correspond au coin supérieur gauche (comme sur le Caneva)
        """
        mat = []
        case = self.taille_quadrillage

        # On commence par créer une matrice nulle de la taille de la carte
        for i in range(0, int(self.taille_carte_y/case)): #boucle "pour chaque ligne du quadrillage"
            ligne = []
            for j in range(0, int(self.taille_carte_x/case)): #boucle "pour chaque colonne du quadrillage"
                ligne.append(0)
            mat.append(ligne)

        # On parcours la liste des plateformes et on remplace par des 1 en conséquence
        for plateforme in self.plateformes:
            x_min, y_min, x_max, y_max = plateforme.get_min_max()
            k = int(x_min/case)
            # On remplace les coefs sur la coordonnée de la plateforme et les suivantes, jusqu'à avoir atteint un mur ou dépassé la plateforme
            while k < (x_max/case) and k < self.taille_carte_x/case:
                mat[int(y_min/case)][k] = 1
                k += 1

        return mat


# Code pour tester et visualiser l'apprence de la matrice de carte quadrillée
"""
decor = Decor(taille_carte_x=2500, taille_carte_y=4000)
decor.creer_decor_hasard()
mat = decor.quadrillage()
for element in mat:
    print(element)
"""