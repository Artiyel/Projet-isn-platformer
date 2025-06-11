import numpy as np
import pygame
from MenuPrincipal import MenuPrincipal
from Elements_Decor import ElementDecor


pygame.init() #startcontroler démarre le jeu donc on initie pygame

class StartControler :
    """
    Met en oeuvre les classes et lance la fenêtre 
    défini la plateforme initiale (la plus basse) cf. Controlleur_Jeu.py
    """

    def __init__(self, jeu, window):
        self.jeu = jeu
        self.window = window 
       #self.plateforme = [ElementDecor(0, self.fenetre.size_y-20, self.fenetre.size_x, self.fenetre.size_y)] #liste des plateformes initiée avec la plateforme de départ
        print("ok")
    
    def execute(self,event):
        if event == "start":
            self.fenetre.running = False
            self.jeu.controleurfenetre.run()


    def start(self) :
        self.fenetre.run() #on lance la fenêtre
        