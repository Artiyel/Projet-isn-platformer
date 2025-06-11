from Fenetre import Fenetre
import pygame
from Button import Button

class MenuInGame(Fenetre):
    def __init__(self, background, window, parent_fenetre_jeu, parent_entities, parent_decor):
        '''classe des menus
        entrée :
            boutons : liste d'instances de Button
            background : image de fond
            window : instance de pygame.display'''
        super().__init__(background, window)
        
        self.etat = "stand by"
        self.parent_fenetre_jeu = parent_fenetre_jeu
        self.parent_entities = parent_entities
        self.parent_decor = parent_decor
        self.button_resume = Button(self.window.get_width() // 2, self.window.get_height() // 2 - 50, 200, 50,"Resume",  (255, 255, 255), (0, 0, 0))
        self.button_quit_game = Button( self.window.get_width() // 2, self.window.get_height() // 2 + 50, 200, 50, "Quit",(255, 255, 255), (0, 0, 0))
        self.button_return_menu = Button(self.window.get_width() // 2, self.window.get_height() // 2 + 150, 200, 50, "Return to Menu", (255, 255, 255), (0, 0, 0))
        self.button_croix = Button(self.window.get_width() - 50, 50, 40, 40, "X",(255, 0, 0), (0, 0, 0))
        

    def draw(self):
        # Affiche le fond capturé (le screenshot du jeu)
        self.window.blit(self.background, (0, 0))
        # Overlay transparent
        overlay = pygame.Surface(self.window.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 120))  # 120 = transparence
        self.window.blit(overlay, (0, 0))
        # Dessine les boutons par-dessus
        self.draw_buttons()

    def draw_buttons(self):
        '''Méthode pour dessiner les boutons sur la fenêtre'''
        self.button_resume.draw(self.window)
        self.button_quit_game.draw(self.window)
        self.button_return_menu.draw(self.window)
        self.button_croix.draw(self.window)
    
    def run(self):
        '''Méthode principale qui gère la boucle du menu en jeu.'''
        self.running = True
        clock = pygame.time.Clock()

        while self.running:

            self.draw()  # dessine le fond et les boutons
            pygame.display.flip()   # met à jour l'affichage
            clock.tick(60)

            for event in pygame.event.get():    # gestion des événements
                if event.type == pygame.QUIT:   # Si l'utilisateur ferme la fenêtre
                    self.running = False
                    self.etat = "quit"
                    pygame.quit()
                    return  

                elif self.button_resume.on_click(event) or self.button_croix.on_click(event):   # Si l'utilisateur clique sur "Resume" ou "X"
                    self.running = False
                    self.etat = "resume"

                elif self.button_quit_game.on_click(event): # Si l'utilisateur clique sur "Quit"
                    self.running = False
                    self.etat = "quit"
                    pygame.quit()  
                    return

                elif self.button_return_menu.on_click(event): # Si l'utilisateur clique sur "Return to Menu"
                    self.running = False
                    self.etat = "retour menu"
                    print("Retour au menu principal demandé")


            # Redessine les boutons à chaque frame pour l'effet hover éventuel
            self.draw()
            self.draw_buttons()
            pygame.display.flip()

