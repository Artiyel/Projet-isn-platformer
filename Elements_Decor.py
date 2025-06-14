class ElementDecor:
    """
    Classe des éléments composant le décor
    Ne comporte ici que les plateformes, mais prévue pour accueillir d'autres types d'éléments
    """
    def __init__(self, x_pos, y_pos, x_taille, y_taille):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_taille = x_taille
        self.y_taille = y_taille

    def __str__(self):
        print(f"L'objet est de taille {self.x_taille} x {self.y_taille} et positionné en ({self.x_pos} ; {self.y_pos})\n")


    def get_min_max(self):
        """
        Méthode permettant d'obtenir les coordonnées des limites de l'objet
        Sous la forme x_min, y_min, x_max, y_max
        """
        return self.x_pos, self.y_pos, self.x_pos + self.x_taille, self.y_pos +self.y_taille
