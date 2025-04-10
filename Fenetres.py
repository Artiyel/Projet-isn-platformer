import pygame

pygame.init()

class Fenetre:
    ''''''
    def __init__(self, background = pygame.image.load("assets/3_isaac.png")):
        #le décor 
        self.background = background

        #paramètre la fenêtre
        self.size_x=self.background.get_width()
        self.size_y=self.background.get_height()

    def affichage(self):
        '''
        entrée : self
        sortie : None
        
        permet de créer l'affichage de la fenêtre
        '''
        #initialisation de la fenêtre
        self.window = pygame.display.set_mode((self.size_x,self.size_y))
        self.window.blit(self.background,(0,0))
        pygame.display.set_caption('Le jeu')

    def affiche_entity(entities):
        for entity in entities:
            ''''''

    def run(self):
        '''
        Entrée : self
        Sortie : None

        Permet de lancer et faire tourner la fenêtre.
        '''
        #on affiche la fenêtre
        self.affichage()

        self.running = True