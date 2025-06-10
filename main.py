# -*- coding: utf-8 -*-
import os
import pygame

import ctypes

from Entity import Player, Fantome
from Decor import Decor
from Game import Game
from copy import deepcopy
from Button import Button
from MenuPrincipal import MenuPrincipal
from MenuInGame import MenuInGame


# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Change the working directory to the script directory
os.chdir(script_dir)



if os.name == 'nt':
    print("ouf!")
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), int(user32.GetSystemMetrics(1)*0.93)
else:
    screensize = (1500,800)
    
window = pygame.display.set_mode(screensize)
fond_menu = pygame.image.load("assets/fond_menu_1.png")
fond_menu = pygame.transform.scale(fond_menu, screensize)
window.blit(fond_menu, (0, 0))
pygame.display.flip()


#ça c'est le main

### PARAMETRES DU JEU ###
taille_carte = (3000,3000)
### CREATION DES ENTITES ###
dict_entites = dict()


#personnage
player = Player()
player.x = 100
player.y = taille_carte[1]
dict_entites["player"] = player

fantome = Fantome()
fantome.x = 200
fantome.y = taille_carte[1]
dict_entites["entites"] = [fantome]

#decor
decor = Decor(taille_carte[0],taille_carte[1])
decor.creer_decor_hasard()
dict_entites["decor"] = decor
#dict_entites["decor"] = []
#for element in decor.plateformes:
#    dict_entites["decor"].append(element)
#print(dict_entites)


fond_menu = pygame.image.load("assets/fond_menu_1.png")
fenetre_menu = MenuPrincipal(background=fond_menu, window=window)
fenetre_menu.draw()
pygame.display.flip()

### CREATION DU JEU ###
game = Game(dict_entites, window)
fenetre_menu.run()

while True:
    if fenetre_menu.etat == 'jeu':
        game.controleurfenetre.run()
        print('run')
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
