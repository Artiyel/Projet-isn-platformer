from FenetreJeu import FenetreJeu
from MenuInGame import MenuInGame
import pygame

pygame.init()

class ControlleurFenetre:
    """
    Classe qui gère la fenêtre de jeu.
    """
    def __init__(self, dict_entites,jeu, window ,background = pygame.image.load("assets/pics/fond_1.png")):
        self.jeu = jeu
        self.fenetre = FenetreJeu(background, window)
        self.controleur = jeu.controleurjeu
        self.decor = dict_entites["decor"]
        self.entities = dict_entites["entites"]
        self.player = dict_entites["player"]
        if self.entities:
            # Assure que fantome est défini même si entities est vide
            self.fantome = self.entities[0] 
        else:
            self.fantome = None  # Assure que fantome est défini même si entities est vide

        self.depl_rel = [0,0]
        self.dir = [0,0]
        fond = background
        self.menu = MenuInGame(
            fond, window,
            parent_fenetre_jeu=self.fenetre,
            parent_entities=self.entities,
            parent_decor=self.decor.plateformes
        )
    

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
            mvt = 5
            self.depl_rel[0]+=mvt*self.dir[0]
            self.depl_rel[1]+=mvt*self.dir[1]
            self.player.x += mvt*self.dir[0]
            self.player.y += mvt*self.dir[1]
            for brick in self.decor.plateformes:
                brick.x_pos += mvt*self.dir[0]
                brick.y_pos += mvt*self.dir[1]
            for ennemy in self.entities:
                ennemy.x += mvt * self.dir[0]
                ennemy.y += mvt * self.dir[1]
            #print("moved")  # Debug : affiche chaque déplacement de l'écran


    def run(self):
        """
        Lance la boucle principale de la fenêtre.
        """
        # self.fenetre.run()
        self.fenetre.draw(decor = self.decor.plateformes)
        pygame.mixer_music.load("assets/music/Celeste_In_The_Mirror.mp3")
        pygame.mixer_music.play(-1)
        etat_saut, etat_right, etat_left = False, False, False
        etat_right_f = False
        etat_left_f = False
        running = True
        arrivee = False
        chute = False
        parcours_chemin = False
        self.chemin = []
        count = 0
        clock = pygame.time.Clock()

        while running and (not arrivee) and (not chute):
            events = pygame.event.get()  #on récupère les événements
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                    self.fenetre.running = False  # Pour arrêter aussi la fenêtre si besoin
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN): 
                    print('test')
                    background_pause = pygame.Surface(self.fenetre.window.get_size())
                    background_pause.blit(self.fenetre.window, (0, 0))
                    self.menu.background = background_pause  # On remplace le fond du menu pause par la capture
                    self.menu.run() #pour lancer un autre menu (qui propose de retourner au menu principal ou continuer le jeu)
                    if self.menu.etat == "retour menu":
                        running = False
                        self.fenetre.running = False 
                        print('ouaippppp')
            #print('event off')

            ###déplacement du fantome
            if self.fantome:
                #on initialise les mouvements à réaliser
                etat_saut_f, etat_right_f, etat_left_f = False, False, False

                #on obtient la position du personnage dans la matrice
                pos_perso = self.controleur.graphe.conversion_reel_to_matrice([self.player.x-self.depl_rel[0],self.player.y-self.depl_rel[1]])

                #on se place sur la plateforme en dessous (le personnage etant en dehors de la plateforme, sa position n'est pas dans le graphe)
                pos_perso[1]+=1

                # de meme pour le fantome            
                pos_fantome = self.controleur.graphe.conversion_reel_to_matrice(
                    [self.fantome.x - self.depl_rel[0], self.fantome.y - self.depl_rel[1]]
                )
                pos_fantome[1] += 1

                # si le fantome n'est pas sur un chemin
                if not parcours_chemin:
                    # on regarde si la position est dans le graphe
                    if str(pos_perso) in self.controleur.graphe.graphe.keys():

                        #dans ce cas, on crée le chemin
                        self.chemin = self.controleur.graphe.chemin_le_plus_court(pos_fantome,pos_perso)

                    #mesure de sécurité
                    if self.chemin != None:
                        parcours_chemin = True

                # si le fantome a un chemin à suivre
                elif self.chemin is not None and self.chemin != []:
                    # on place l'objectif à la prochaine étape du chemin
                    obj_rel = [int(x) for x in self.chemin[0].strip("[]").split(",")]
                    objectif = self.controleur.graphe.conversion_matrice_to_reel(obj_rel)
                    objectif[0]-=self.depl_rel[0]
                    objectif[1]-=self.depl_rel[1]

                    #on regarde les actions nécessaires
                    if pos_fantome[0] - obj_rel[0] > 0:
                        etat_left_f = True
                    if obj_rel[0] - pos_fantome[0] > 0:
                        etat_right_f = True
                    if pos_fantome[1] - obj_rel[1] > 0:
                        etat_saut_f = True
                        count+=1

                    # si on a atteint l'objectif, on passe au suivant
                    if (abs(pos_fantome[0] - obj_rel[0]) == 0 and abs(obj_rel[1] - pos_fantome[1]) < 50):
                        self.chemin.pop(0)
                        count = 0

                # si on a atteint le personnage, on clear le chemin
                if (pos_fantome[0] - pos_perso[0] == 0 and pos_perso[1] - pos_fantome[1] == 0) or self.chemin == [] or count > 20:
                    self.chemin = None
                    parcours_chemin = False
                    count = 0

            self.move_all()  # Déplace tout si besoin (scrolling)

            # On vérifie la condition de victoire "joueur sur la plateforme d'arrivee"
            Plateforme_fin = self.decor.plateformes[-1]
            if (
                (self.player.x >= Plateforme_fin.x_pos) and
                (self.player.x + self.player.x_taille <= Plateforme_fin.x_pos + Plateforme_fin.x_taille) and
                (self.player.y + self.player.y_taille <= Plateforme_fin.y_pos + Plateforme_fin.y_taille) and
                (self.player.y + self.player.y_taille >= Plateforme_fin.y_pos - 5)
            ):
                self.fenetre.textbox("assets/text/1t.txt")
                arrivee = True
                # Lance le menu in-game après le texte
                self.menu.etat = "stand by"  # Réinitialise l'état du menu
                self.menu.running = True
                self.menu.run()
                # Après le menu, tu peux agir selon l'état choisi par l'utilisateur
                if self.menu.etat == "return to menu":
                    running = False
                    self.fenetre.running = False
                elif self.menu.etat == "quit":
                    running = False
                    self.fenetre.running = False
                    pygame.quit()
                    exit()

            # On vérifie la condition de fin de partie "Le joueur est tombé de la carte"
            if self.player.y > self.decor.plateformes[0].y_pos + 500:
                self.fenetre.textbox("assets/text/Stubborn3ss.txt")
                chute = True
                # Lance le menu in-game après le texte
                self.menu.etat = "stand by"  # Réinitialise l'état du menu
                self.menu.running = True
                self.menu.run()
                # Après le menu, tu peux agir selon l'état choisi par l'utilisateur
                if self.menu.etat == "return to menu":
                    running = False
                    self.fenetre.running = False
                elif self.menu.etat == "quit":
                    running = False
                    self.fenetre.running = False
                    pygame.quit()
                    exit()

            # On passe events à souhait_action_joueur
            etat_saut, etat_right, etat_left = self.controleur.souhait_action_joueur(
                etat_saut, etat_right, etat_left, events
            )
            if self.fantome:
                # On passe events à souhait_action_fantome
                etat_right_f, etat_left_f = self.controleur.souhait_action_fantome(etat_right_f,etat_left_f)
 
            self.controleur.calcul_mvt(etat_saut, etat_right, etat_left,self.player)
            if self.fantome:
                # On calcule le mouvement du fantôme
                self.controleur.calcul_mvt(etat_saut_f, etat_right_f, etat_left_f,self.fantome)
    
            #important de mettre du délai. Là on a 60fps.
            clock.tick(60)  # 60 FPS, fluide

            # Affichage
            self.fenetre.draw(decor=self.decor.plateformes, entities=[self.player, self.fantome])
            #Et voilà le job du controlleur. On récupère toutes les actions...
            
            #NE PAS OUBLIER LE DISPLAY.FLIP() SINON CA VA FAIRE TOUT NOIR
            pygame.display.flip()
        pygame.mixer_music.stop()
        if arrivee:
            print("Le joueur a gagné")
        if chute:
            print("Le joueur est tombé de la carte")
