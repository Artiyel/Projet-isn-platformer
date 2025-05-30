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
        self.dir = [0,0]

    def should_move(self):
        """
        gestion des déplacements de l'écran
        :return: si on est offlimit -> True si l'écran doit bouger, False sinon
        """
        #on cherche dans quelle direction il faudrait déplacer l'écran
        if self.player.x < self.fenetre.screensize[0]/3:
            self.dir[0] = 1
            offlimit = True
        elif self.player.x > self.fenetre.screensize[0]*2/3:
            self.dir[0]=-1
            offlimit = True
        else :
            self.dir[0]=0
            offlimit = False
        if self.player.y < self.fenetre.screensize[1]/3:
            self.dir[1] = 1
            offlimit = True
        elif self.player.y > self.fenetre.screensize[1]*2/3:
            self.dir[1]=-1
            offlimit = True
        else :
            self.dir[1]=0
            offlimit = False
        
        #on regarde si on est offlimits
        if self.player.x < self.fenetre.screensize[0]/4 or self.player.x > self.fenetre.screensize[0]*3/4 or self.player.y < self.fenetre.screensize[1]/4 or self.player.y > self.fenetre.screensize[1]*3/4:
            offlimit = True

        return offlimit

    def move_all(self):
        """
        on bouge tout si on est offlimit
        """
        while self.should_move():
            self.player.x += 10*self.dir[0]
            self.player.y += 10*self.dir[1]
            for brick in self.decor:
                brick.x_pos += 10*self.dir[0]
                brick.y_pos += 10*self.dir[1]
            for ennemy in self.entities:
                ennemy.x += 10 * self.dir[0]
                ennemy.y += 10 * self.dir[1]
            print("moved")  # Debug : affiche chaque déplacement de l'écran

    def run(self):
        """
        Lance la boucle principale de la fenêtre.
        """
        # self.fenetre.run()
        self.fenetre.draw(decor = self.decor)
        pygame.mixer_music.load("assets/music/Celeste_In_The_Mirror.mp3")
        etat_saut, etat_right, etat_left = False, False, False
        running = True
        while running:
            events = pygame.event.get()  #on récupère les événements
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                    self.fenetre.running = False  # Pour arrêter aussi la fenêtre si besoin
            self.move_all()  # Déplace tout si besoin (scrolling)
            if not pygame.mixer_music.get_busy():
                # Si la musique n'est pas en cours de lecture, on la lance
                pygame.mixer_music.play()
            pygame.mixer_music.set_volume(1)
            # On passe events à souhait_action_joueur
            etat_saut, etat_right, etat_left = self.controleur.souhait_action_joueur(etat_saut, etat_right, etat_left, events)
            self.controleur.calcul_mvt(etat_saut, etat_right, etat_left)
            #important de mettre du délai. Là on a une image tout les 20ms, donc 50fps.
            pygame.time.delay(20)
            #On utilise cette méthode pour afficher la fenêtre dans la boucle (interdiction d'utiliser .run() ici)
            self.fenetre.draw(decor=self.decor, entities=[self.player])
            #Et voilà le job du controlleur. On récupère toutes les actions...
            
            #NE PAS OUBLIER LE DISPLAY.FLIP() SINON CA VA FAIRE TOUT NOIR
            pygame.display.flip()
        pygame.quit()