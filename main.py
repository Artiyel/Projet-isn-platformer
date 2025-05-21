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

### CREATION DES ENTITES ###
perso = deepcopy(Player())
decor = Decor()

### CREATION DU JEU ###
game = Game()