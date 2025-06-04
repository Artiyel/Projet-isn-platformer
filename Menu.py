from Fenetre import Fenetre
import pygame

class Menu(Fenetre):
    def __init__(self, background, window):
        super.__init__(self,background, window)

    def draw(self):
        super.draw()
        #et genre là faut mettre les boutons appropriés mais je comprends pas comment ça a été fait jksdfjslk
    
    def run(self):
        self.window.blit(self.background,(0,0))
        pygame.display.set_caption('Le jeu')
        #on affiche la fenêtre
        self.draw()

        self.running = True

        while self.running:

            events = pygame.event.get()

            for event in events:
                if event.type 
