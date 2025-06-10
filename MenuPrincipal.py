import pygame
from Fenetre import Fenetre
from Button import Button
import Game 


class MenuPrincipal(Fenetre):
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
        clock = pygame.time.Clock()
        self.draw()
        self.running = True
        pygame.mixer_music.load("assets/music/NieR_WotW.mp3")
        pygame.mixer_music.play(-1)
        while self.running:
            # on regarde si le joueur a cliqué sur un bouton
            for event in pygame.event.get():
                #on arrête le jeu si on quitte par la croix par défaut (ou le bouton rouge pour les mac)
                if event.type == pygame.QUIT:
                    self.running = False
                    self.etat = "quit"
                                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("1")
                    for button in self.buttons:
                        print("2")
                        if button.is_hit(pygame.mouse.get_pos()):
                            if button.text == "Start Game":
                                self.etat = "jeu"
                                self.mode = "classique"
                                self.running = False    #quitte la fenêtre du menu
                                print("3")
                                self.etat = "jeu"
                            elif button.text == "Mode Fantôme":
                                self.etat = "jeu"
                                self.mode = "fantome"
                                self.running = False
                                print("Mode Fantôme activé")
                            elif button.text == "Quit":
                                self.etat = "quit"
                                self.running = False
                                print("Quitter le jeu")
                            elif button.text == "Histoire":
                                self.etat = "lore"
                                print("Histoire du jeu")
                                self.running = False
                                # Crée une nouvelle fenêtre pour le lore
                                fond_lore = pygame.image.load("assets//pics/fond_menu_1.png")
                                print("Fond lore chargé :", fond_lore.get_size())
                                fenetre_lore = MenuPrincipal(background=fond_lore, window=self.window)
                                fenetre_lore.draw()  # Affiche la fenêtre avec le fond
                                pygame.display.flip()
                                pygame.time.wait(2000)
                                # fenetre_lore = FenetreMenu()  # ou Fenetre(background=...) si tu veux un fond différent
                                fenetre_lore.textbox("lore.txt")  # Affiche le texte dans la nouvelle fenêtre
                                self.fenetre.running = True
                                self.start()
                            elif button.text == "Mode Fantôme":
                                self.etat = "fantome"
                                print("Mode Fantôme activé")
            self.draw()
            pygame.display.flip()
            clock.tick(60)  # 60 FPS

        pygame.mixer_music.stop()