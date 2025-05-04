import numpy as np
import pygame
from Fenetres import * 


pygame.init() #startcontroler démarre le jeu donc on initie pygame

class StartControler :
    """
    Met en oeuvre les classes et lance la fenêtre 
    défini la plateforme initiale (la plus basse) cf. Controlleur_Jeu.py
    """

    def __init__(self) :
        self.fenetre = Fenetre() #création de la fenêtre du menu principal
        self.plateforme = [Elements_Decor(0, self.fenetre.size_y-20, self.fenetre.size_x, self.fenetre.size_y)] #liste des plateformes initiée avec la plateforme de départ

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

                    

                    
                
    
control = StartControler()
control.start()
