# -*- coding: utf-8 -*-
import os
# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Change the working directory to the script directory
os.chdir(script_dir)

import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


from Entity import Player, Fantome
from Decor import Decor
from Game import Game
from copy import deepcopy
from Button import Button

#ça c'est le main

### PARAMETRES DU JEU ###
taille_carte = (3000,50000)
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


#entites non jouables
from Entity import Fantome

fantome = Fantome()
fantome.x = 200
fantome.y = 4950
dict_entites["entites_non_jouables"] = [fantome]

###BOUTONS###
buttons = []

#bouton start
size = (200,50)
bouton_start = Button(screensize[0] //2,screensize[1]//2,size[0],size[1],"Start Game")
buttons.append(bouton_start)
bouton_lore = Button(screensize[0] //2,screensize[1]//2+100,size[0],size[1],"Histoire")
buttons.append(bouton_lore)
bouton_mode_fantome = Button(screensize[0] //2,screensize[1]//2+200,size[0],size[1],"Mode Fantôme")
buttons.append(bouton_mode_fantome)
#bouton quit
bouton_quit = Button(screensize[0] //2,screensize[1]//2+300,size[0],size[1],"Quit")
buttons.append(bouton_quit)

### CREATION DU JEU ###
game = Game(dict_entites,buttons)
game.startcontroler.start()