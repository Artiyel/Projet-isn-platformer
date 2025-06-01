import pygame
from Fenetre import Fenetre

class FenetreMenu(Fenetre):
    def __init__(self, background = pygame.image.load("assets/fond_1.png"), buttons = []):
        super(FenetreMenu,self).__init__(background)
        self.buttons = buttons
        print("Taille de la fenêtre :", self.window.get_width(), "x", self.window.get_height())

    def draw_buttons(self):
        #on dessine les boutons
        for button in self.buttons:
            button.draw(self.window)
    
    def draw(self):
        # #on dessine les éléments de base
        # super().draw()
        # #on affiche les boutons
        # self.draw_buttons()   
        self.window.fill((30, 30, 60))  # fond bleu foncé
        font = pygame.font.SysFont("Arial", 48)
        titre = font.render("Plateformer ISN", True, (255, 255, 255))
        self.window.blit(titre, (100, 50))
        # Affiche les boutons
        for bouton in self.buttons:
            bouton.draw(self.window)