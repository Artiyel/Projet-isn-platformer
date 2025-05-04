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



    def test_contact(self):
        print("stuff to do")


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

    def calcul_mvt(self):
        ''' méthode qui effectue tous les tests avec les méthodes faites en haut et renvoie la position finale du joueur
        peut être que y'a pas besoin de renvoie et qu'on peut juste update la position dans l'instance perso directement mais pas sûr que ça marche!'''
        #... y'a masse trucs à rajouter là 
        chose_a_rajouter = True
        if chose_a_rajouter:
            print("il manque des trucs")
        else:
        pos_x = self.perso.potentiel_pos_x
        pox_y = self.peros.potentiel_pos_y
        return pos_x, pos_y #peut être que y'en a pas besoin en vrai


    
    def gravite(self) :
            """
            Gère la gravité du personnage
            """
            #on regarde si le personnage est sur le sol ou pas, et on applique la gravité en conséquence
            while test_contact_plateforme(self.fenetre.player) == False: 
                # on applique la gravité au personnage
                self.fenetre.player.rect.y += 2
                # ici, on considère que le perso peut descendre en dehors de la fenêtre de jeu affichée (il peut régresser)
                # on considère que le point de départ (tout en bas) est sur une plateforme qu'il faudra penser à crééer en début de jeu
