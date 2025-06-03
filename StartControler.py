import numpy as np
import pygame
from FenetreMenu import FenetreMenu
from Elements_Decor import ElementDecor



pygame.init() #startcontroler démarre le jeu donc on initie pygame

class StartControler :
    """
    Met en oeuvre les classes et lance la fenêtre 
    défini la plateforme initiale (la plus basse) cf. Controlleur_Jeu.py
    """

    def __init__(self, jeu, buttons, window):
        self.jeu = jeu
        self.window = window 
        self.fenetre = FenetreMenu(pygame.image.load("assets/fond_menu_1.png"), window, buttons=buttons)
        #self.plateforme = [ElementDecor(0, self.fenetre.size_y-20, self.fenetre.size_x, self.fenetre.size_y)] #liste des plateformes initiée avec la plateforme de départ
        print("ok")
        self.draw(buttons)

    def draw(self,buttons):
        for button in buttons:
            print(button)
            win = self.fenetre.window
            button.draw(win)

    def execute(self,event):
        if event == "start":
            self.fenetre.running = False
            self.jeu.controleurfenetre.run()

    def start(self) :
        self.fenetre.run() #on lance la fenêtre
        while self.fenetre.running:
            pygame.time.delay(5)
            pygame.display.flip()
            #on regarde si le joueur exécute des actions
            for event in pygame.event.get():
                #on arrête le jeu si on quitte par la croix par défaut (ou le bouton rouge pour les mac)
                if event.type == pygame.QUIT:
                    self.fenetre.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("1")
                    for button in self.fenetre.buttons:
                        print("2")
                        if button.is_hit(pygame.mouse.get_pos()):
                            if button.text == "Start Game":
                                self.fenetre.running = False    #quitte la fenêtre du menu
                                print("3")
                                self.jeu.controleurfenetre.run()  # lance la fenêtre de jeu
                            elif button.text == "Quit":
                                self.fenetre.running = False
                                print("Quitter le jeu")
                            elif button.text == "Histoire":
                                print("Histoire du jeu")
                                self.fenetre.running = False
                                # Crée une nouvelle fenêtre pour le lore
                                fond_lore = pygame.image.load("assets/fond_menu_1.png")
                                print("Fond lore chargé :", fond_lore.get_size())
                                fenetre_lore = FenetreMenu(background=fond_lore, window=self.window)
                                fenetre_lore.draw()  # Affiche la fenêtre avec le fond
                                pygame.display.flip()
                                pygame.time.wait(2000)
                                # fenetre_lore = FenetreMenu()  # ou Fenetre(background=...) si tu veux un fond différent
                                fenetre_lore.textbox("lore.txt")  # Affiche le texte dans la nouvelle fenêtre
                                self.fenetre.running = True
                                self.start()
                            elif button.text == "Mode Fantôme":
                                print("Mode Fantôme activé")