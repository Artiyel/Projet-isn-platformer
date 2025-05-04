from Decor import Decor


class ControleurJeu:

    def __init__(self, decor, perso, liste_ennemis):
        self.decor = decor
        self.perso = perso
        self.liste_ennemis= liste_ennemis

    def test_contact_plateforme(self, entite):
        for element in self.decor.plateformes:
            x_min, y_min, x_max, y_max = element.get_min_max()
            if self.perso.y_pos + self.perso.y_taille == y_min
                and self.perso.x_pos < x_max
                and self.perso.x_pos + self.perso.x_taille > x_max:
                res =



    def test_contact