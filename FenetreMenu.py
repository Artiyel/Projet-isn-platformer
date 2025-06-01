import pygame
from Fenetre import Fenetre

class FenetreMenu(Fenetre):
    def __init__(self, background = pygame.image.load("assets/fond_menu_1.png"), buttons = []):
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

        font = pygame.font.SysFont("Chiller", 200, bold=True)
        titre = font.render("ICI", True, (255, 167, 17))
        text_rect = titre.get_rect(center=(self.window.get_width() // 2, 250))
        self.window.blit(titre, text_rect)

        # Affiche les boutons
        for bouton in self.buttons:
            bouton.draw(self.window)