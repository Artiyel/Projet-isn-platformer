import numpy as np
import pygame
from Fenetres import * 


pygame.init() #startcontroler démarre le jeu donc on initie pygame

class StartControler :
    """
    Met en oeuvre les classes et lance la fenêtre
    """

    def __init__(self) :
        self.fenetre = Fenetre() #création de la fenêtre du menu principal

    def start(self) :
        self.fenetre.run() #on lance la fenêtre
        while self.fenetre.running:
            pygame.time.delay(20)
            pygame.display.flip()
            #on regarde si le joueur exécute des actions
            for event in pygame.event.get():
                #on arrête le jeu si on quitte par la croix par défaut (ou le bouton rouge pour les mac)
                if event.type == pygame.QUIT:
                    self.fenetre.running = False
                #on regarde si le joueur demande à bouger, puis on check là où il est pour savoir ce qu'il se passe (il tombe, y'a un mur, y'a un ennemi)
                #et après/simultanément, on gère l'affichage
                "if ..."
                
    
control = StartControler()
control.start()
