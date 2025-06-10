from Fenetre import Fenetre
import pygame
from Button import Button

class MenuInGame(Fenetre):
    def __init__(self, background, window):
        '''classe des menus
        entrée :
            boutons : liste d'instances de Button
            background : image de fond
            window : instance de pygame.display'''
        super().__init__(background, window)
        self.button_resume = Button(self.window.get_width() // 2, self.window.get_height() // 2 - 50, 200, 50,"Resume",  (255, 255, 255), (0, 0, 0))
        self.button_quit_game = Button( self.window.get_width() // 2, self.window.get_height() // 2 + 50, 200, 50, "Quit",(255, 255, 255), (0, 0, 0))
        self.button_return_menu = Button(self.window.get_width() // 2, self.window.get_height() // 2 + 150, 200, 50, "Return to Menu", (255, 255, 255), (0, 0, 0))
        self.button_croix = Button(self.window.get_width() - 50, 50, 40, 40, "X",(255, 0, 0), (0, 0, 0))
        

    def draw(self):
        super().draw()
        
    
    def draw_buttons(self):
        self.button_resume.draw(self.window)
        self.button_quit_game.draw(self.window)
        self.button_return_menu.draw(self.window)
        self.button_croix.draw(self.window)
    
    def run(self):
        self.window.blit(self.background, (0, 0))
        pygame.display.set_caption('Le jeu')

        self.draw()
        self.draw_buttons()
        pygame.display.flip()
        self.running = True
        self.etat = "stand by"

        while self.running:
            pygame.time.delay(5)  # Pour la fluidité, tu peux remplacer par un clock.tick(60) si tu veux
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                    self.etat = "quit"
                    pygame.quit()  

                elif (self.button_resume.is_hit(pygame.mouse.get_pos()) or self.button_croix.is_hit(pygame.mouse.get_pos())):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.running = False
                        self.etat = "resume"

                elif self.button_quit_game.is_hit(pygame.mouse.get_pos()):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.running = False
                        self.etat = "quit"
                        pygame.quit() 

                elif self.button_return_menu.is_hit(pygame.mouse.get_pos()):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.running = False
                        self.etat = "retour menu"
                        print("Retour au menu principal demandé")


            # Redessine les boutons à chaque frame pour l'effet hover éventuel
            self.draw()
            self.draw_buttons()
            pygame.display.flip()

