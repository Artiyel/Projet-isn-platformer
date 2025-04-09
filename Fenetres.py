import pygame

pygame.init()

class fenetre:
    ''''''
    def __init__(self):
        #le décor 
        self.background = pygame.image.load("assets/3_isaac.png")

        #paramètre la fenêtre
        self.size_x=self.background.get_width()
        self.size_y=self.background.get_height()
        pygame.display.set_caption("Squarey")

    def affichage(self):
        '''
        entrée : self
        sortie : None
        
        permet de créer l'affichage de la fenêtre
        '''
        #initialisation de la fenêtre
        self.window = pygame.display.set_mode((self.size_x,self.size_y))
        self.window.blit(self.background,(0,0))
        pygame.display.set_caption('RPG UwU')

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
    
#qouicoubeh
