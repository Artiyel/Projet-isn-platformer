fimport pygame

pygame.init()

class Entity:
    def __init__(self):
        self.x = 0
        self.y = 0

class Player(Entity):
    def __init__(self):
        super.__init__()

    def bouger(self,ajout_x, ajout_y):
        '''recupère une info donnée par le controlleur sur de combien il doit bouger et update les variables self.x et self.y'''
        self.x += ajout_x
        self.y += ajout_y
     

class Ennemy(Entity):
    def __init__(self):
        super.__init__()
