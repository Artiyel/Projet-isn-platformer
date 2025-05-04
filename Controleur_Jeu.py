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

    def souhait_action(self):
    #récupère l'information du déplacement/ de l'action (si jamais on en ajoute) que veut effectuer le joueur
    for event in pygame.event.get():
        saut = 10 #nombre de pixel que fait bouger un saut
        mvt = 5 #nombre de pixel que fait bouger un déplacement
        if event.type == pygame.KEYDOWN: #recup l'information du clavier du joueur 
            if event.key == pygame.K_UP:
                self.perso.potentiel_pos_y = self.perso.y - saut
            if event.key == pygame.K_RIGHT:
                self.perso.potentiel_pos_x = self.perso.x + mvt
            if event.key == pygame.K_LEFT:
                self.perso.potentiel_pos_x = self.perso.x - mvt
