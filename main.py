# -*- coding: utf-8 -*-
import os
import pygame

import ctypes

from Entity import Player, Fantome
from Decor import Decor
import Game
from copy import deepcopy
from Button import Button
from MenuPrincipal import MenuPrincipal
from MenuInGame import MenuInGame


# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Change the working directory to the script directory
os.chdir(script_dir)


# gestion de la taille de l'écran en fonction de l'OS (Windows ou Linux)
if os.name == 'nt':
    print("ouf!")
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), int(user32.GetSystemMetrics(1)*0.93)
else:
    screensize = (1500,800)

# On définits les assets importés
window = pygame.display.set_mode(screensize)
pygame.display.set_caption("ICI")
fond_menu = pygame.image.load("assets/pics/fond_menu_1.png")
fond_menu = pygame.transform.scale(fond_menu, screensize)
window.blit(fond_menu, (0, 0))
pygame.display.flip()



### PARAMETRES DU JEU ###
taille_carte = (3000,20000)

fond_menu = pygame.image.load("assets/pics/fond_menu_1.png")
fenetre_menu = MenuPrincipal(background=fond_menu, window=window)
fenetre_menu.draw()
pygame.display.flip()

#Programme de lancement
fenetre_menu.run()

### gestion des différents états du jeu ###
while True:
    if fenetre_menu.etat == 'quit':
        print('quitter le jeu')
        pygame.quit()
        break

    if fenetre_menu.etat == 'jeu':
        if fenetre_menu.mode == 'classique':
            print('mode classique')
            game = Game.Game("classique", window, taille_carte)
        elif fenetre_menu.mode == 'fantome':
            print('mode fantome')
            game = Game.Game("fantome", window, taille_carte)
        game.initialize_controlers(window)
        game.controleurfenetre.run()

        # Après la partie, on regarde ce que l'utilisateur veut faire
        if game.controleurfenetre.menu.etat == "retour menu":
            print('retour au menu')
            fenetre_menu.run()
            
        elif game.controleurfenetre.menu.etat == 'quit':
            print('quitter le jeu')
            pygame.quit()
            break

    elif fenetre_menu.etat == 'lore':
        print('lore time')

    elif fenetre_menu.etat == 'fantome':
        print('mode fantome ouais')
