from FenetreJeu import FenetreJeu
import pygame

pygame.init()

class ControlleurFenetre:
    """
    Classe qui gère la fenêtre de jeu.
    """
    def __init__(self, decor, entities, player,jeu ,background = pygame.image.load("assets/3_isaac.png")):
        self.jeu = jeu
        self.fenetre = FenetreJeu(background)
        self.controleur = jeu.controleurjeu
        self.decor = decor.plateformes
        self.entities = entities
        self.player = player
        self.dir = (0,0)

    def should_move(self):
        """
        gestion des déplacements de l'écran
        :return: si on est offlimit -> True si l'écran doit bouger, False sinon
        """
        
        #on cherche dans quelle direction il faudrait déplacer l'écran
        if self.player.x < self.fenetre.screensize[0]/3:
            self.dir[0] = 1
        elif self.player.x > self.fenetre.screensize[0]*2/3:
            self.dir[0]=-1
        if self.player.y < self.fenetre.screensize[1]/3:
            self.dir[1] = 1
        elif self.player.y > self.fenetre.screensize[1]*2/3:
            self.dir[1]=-1
        else :
            offlimit = False
        
        #on regarde si on est offlimits
        if self.player.x < self.fenetre.screensize[0]/4 or self.player.x > self.fenetre.screensize[0]*3/4 or self.player.y < self.fenetre.screensize[1]/4 or self.player.y > self.fenetre.screensize[1]*3/4:
            offlimit = True

        return offlimit
        

    def move_all(self):
        """
        on bouge tout si on est offlimit
        """
        if self.should_move():
            self.player.x += self.dir[0]
            self.player.y += self.dir[1]
            for brick in self.decor:
                brick.x_pos += self.dir[0]
                brick.y_pos += self.dir[1]
            for ennemy in self.entities:
                ennemy.x += self.dir[0]
                ennemy.y += self.dir[1]


    def run(self):
        """
        Lance la boucle principale de la fenêtre.
        """
        self.fenetre.run()
        self.fenetre.draw(decor = self.decor)
        pygame.mixer_music.load("assets/music/Celeste_In_The_Mirror.mp3")
        etat_saut, etat_right, etat_left = False,False,False
        #la boucle principale
        while self.fenetre.running:
            if pygame.mixer_music.get_busy() == False:
                pygame.mixer_music.play()
            pygame.mixer_music.set_volume(1)
            etat_saut, etat_right, etat_left = self.controleur.souhait_action(etat_saut, etat_right, etat_left)
            self.controleur.calcul_mvt(etat_saut, etat_right, etat_left)
            #important de mettre du délai. Là on a une image tout les 20ms, donc 50fps.
            pygame.time.delay(20)
            #On utilise cette méthode pour afficher la fenêtre dans la boucle (interdiction d'utiliser .run() ici)
            self.fenetre.draw(decor=self.decor, entities=[self.player])
            #Et voilà le job du controlleur. On récupère toutes les actions...
            for event in pygame.event.get():
                #... et on  exécute les trucs qu'on veut.
                if event.type == pygame.QUIT:
                    self.fenetre.running = False
                    pygame.mixer_music.stop()
                if event.type == pygame.KEYDOWN:
                    key = pygame.key.get_pressed()
                    if key[pygame.K_m]:
                        self.fenetre.textbox("assets/text/y0u.txt")
                    if key[pygame.K_t]:
                        self.fenetre.textbox("assets/text/1t.txt")
            
            #NE PAS OUBLIER LE DISPLAY.FLIP() SINON CA VA FAIRE TOUT NOIR
            pygame.display.flip()