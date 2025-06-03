from Elements_Decor import ElementDecor

class Plateforme(ElementDecor):
    """
    classe des plateformes
    hérite de la classe ElementDecor
    """
    def __init__(self, x_pos, y_pos, x_taille = 100, y_taille = 10):
        super().__init__(x_pos, y_pos, x_taille, y_taille)
        self.arrivee = False

    def __str__(self):
        print(f"L'objet est une plateforme \n")
        super().__str__()