import pygame
from Fenetre import Fenetre
from Button import Button
import Game 


class MenuPrincipal(Fenetre):
    '''Classe représentant le menu principal du jeu, hérite de Fenetre et gère 
        l'affichage des boutons et les interactions de l'utilisateur.
    '''
    def __init__(self, background, window):
        super().__init__(background, window)
        self.etat = "stand by"
        
        self.buttons = []
        self.bouton_start = Button(self.window.get_width() // 2, self.window.get_height() // 2, 200, 50,"Start Game")
        self.buttons.append(self.bouton_start)
        self.bouton_lore = Button(self.window.get_width() // 2, self.window.get_height() // 2+100,200, 50,"Histoire")
        self.buttons.append(self.bouton_lore)
        self.bouton_mode_fantome = Button(self.window.get_width() // 2, self.window.get_height() // 2+200,200, 50,"Mode Fantôme")
        self.buttons.append(self.bouton_mode_fantome)
        self.bouton_quit = Button(self.window.get_width() // 2, self.window.get_height() // 2+300,200, 50,"Quit")
        self.buttons.append(self.bouton_quit)

        print("Taille de la fenêtre :", self.window.get_width(), "x", self.window.get_height())

    def draw_buttons(self):
        #on dessine les boutons
        for button in self.buttons:
            button.draw(self.window)
    
    def draw(self):
        super().draw()
        # affichage titre du jeu 
        font = pygame.font.SysFont("Chiller", 200, bold=True)   # police et taille
        titre = font.render("ICI", True, (255, 167, 17))    # texte et couleur
        text_rect = titre.get_rect(center=(self.window.get_width() // 2, 250))  # position texte (centrage + pos.vrticale)
        # on centre le titre        
        self.window.blit(titre, text_rect)

        # Affiche les boutons
        for bouton in self.buttons:
            bouton.draw(self.window)
    
    def run(self):
        '''Méthode principale qui gère la boucle du menu principal.'''
        clock = pygame.time.Clock()
        self.draw()
        self.running = True
        pygame.mixer_music.load("assets/music/NieR_WotW.mp3")
        pygame.mixer_music.play(-1)

        while self.running:
            # gestion des interactions de l'utilisateur avec l'interface
            for event in pygame.event.get():
                if event.type == pygame.QUIT:       # Si l'utilisateur ferme la fenêtre
                    self.running = False
                    self.etat = "quit"

                for button in self.buttons:

                    if button.on_click(event):     # Si l'utilisateur clique sur un bouton

                        if button.text == "Start Game":     # Si "Start Game" est cliqué
                            self.etat = "jeu"
                            self.mode = "classique"
                            self.running = False

                        elif button.text == "Mode Fantôme":
                            self.etat = "jeu"
                            self.mode = "fantome"
                            self.running = False

                        elif button.text == "Quit":
                            self.etat = "quit"
                            self.running = False
                        
                        elif button.text == "Histoire":
                            self.etat = "lore"
                            self.running = False
                            # création d'une nouvelle fenêtre pour le lore
                            fond_lore = pygame.image.load("assets//pics/fond_menu_1.png")   # chargement de l'image de fond
                            fenetre_lore = MenuPrincipal(background=fond_lore, window=self.window)  # création de la fenêtre
                            fenetre_lore.draw() # dessine la fenêtre
                            pygame.display.flip() # met à jour l'affichage
                            pygame.time.wait(2000)
                            fenetre_lore.textbox("assets/text/lore.txt") # affiche le texte du lore via une méthode de la classe Fenetre
                            # Après avoir affiché le lore, on revient au menu principal
                            self.running = True
                            self.run()

            # dessine et met à jour l'affichage
            self.draw()
            pygame.display.flip()
            clock.tick(60)  # 60 FPS

        # Arrête la musique avant de quitter
        pygame.mixer_music.stop()