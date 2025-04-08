import pygame

pygame.init()

class Entity:
    def __init__(self):
        self.x = 0
        self.y = 0

class Player(Entity):
    def __init__(self):
        super.__init__()

class Ennemy(Entity):
    def __init__(self):
        super.__init__()