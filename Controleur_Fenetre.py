from FenetreJeu import FenetreJeu
import pygame

pygame.init()

class ControlleurFenetre:
    """
    Classe qui gère la fenêtre de jeu.
    """
    def __init__(self, background, decor, entities, player):
        self.fenetre = FenetreJeu(background)
        self.decor = decor
        self.entities = entities
        self.player = player
        self.dir = (0,0)

    def should_move(self):
        
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
        self.running = True
        while self.running:
            pygame.time.delay(20)
            self.move_all()
            self.fenetre.draw(self.entities, self.decor)
            for event in self.fenetre.get_events():
                if event.type == self.fenetre.QUIT:
                    self.running = False