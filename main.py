# -*- coding: utf-8 -*-
import os
# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Change the working directory to the script directory
os.chdir(script_dir)


from Entity import *
from Decor import Decor
from Game import Game
from copy import deepcopy

#ça c'est le main

### PARAMETRES DU JEU ###
taille_carte = (1000,5000)
### CREATION DES ENTITES ###
dict_entites = dict()

#personnage
perso = deepcopy(Player())
dict_entites["player"] = perso

#decor
decor = Decor(taille_carte[0],taille_carte[1])
decor.creer_decor_hasard()
dict_entites["decor"] = []
for element in decor.plateformes:
    dict_entites["decor"].append(element)
    print(element)
print(dict_entites)

#entites
dict_entites["entites"] = []


### CREATION DU JEU ###
game = Game(dict_entites)