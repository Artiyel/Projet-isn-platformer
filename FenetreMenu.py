import pygame
from Fenetre import Fenetre

class FenetreMenu(Fenetre):
    def __init__(self, background = pygame.image.load("assets/3_isaac.png"), buttons = []):
        super(FenetreMenu,self).__init__(background)
        self.buttons = buttons

    def draw_buttons(self):
        #on dessine les boutons
        for button in self.buttons:
            button.draw(self.window)
    
    def draw(self):
        #on dessine les éléments de base
        super().draw()
        #on affiche les boutons
        self.draw_buttons()   