from Elements_Decor import ElementDecor

class Plateforme(ElementDecor):
    """

    """
    def __init__(self, x_pos, y_pos, x_taille, y_taille):
        super().__init__(x_pos, y_pos, x_taille, y_taille)

    def __str__(self):
        print(f"L'objet est une plateforme \n")
        super().__str__()


