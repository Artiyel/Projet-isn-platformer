import pygame
from Fenetre import Fenetre

class FenetreMenu(Fenetre):
    def __init__(self, background = pygame.image.load("assets/3_isaac.png")):
        super.__init__(background)

    def draw_buttons(self,buttons):
        for button in buttons:
            button.draw(self.window)
    
    def draw(self):
        super().draw()
        self.draw_buttons()