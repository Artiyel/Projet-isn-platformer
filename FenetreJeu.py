from Fenetre import Fenetre
import pygame

class FenetreJeu(Fenetre):
    '''
    Gere l'affichage de 
    '''
    def __init__(self,background = pygame.image.load("assets/3_isaac.png")):
        super.__init__(background)

    def draw_entity(self,entities):
        '''
        input :
            - self
            - entities :
                liste de dict {id : "nom", pos : (posx,posy), taille : (taille_x,taille_y)}
                
        output : None
        
        affiche toutes les entités présentes
        '''
        for entity in entities:
            img = pygame.image.load(f"assets/characters/{entity["id"]}")
            img = pygame.transform.scale(img,entity["taille"])
            self.window.blit(img,entity["pos"])

    def draw_decor(self,decor):
        '''
        input :
            - self
            - decor :
                liste des éléments de décor sous la forme (WIP)
                
        Affiche les éléments du décor
        '''
        for element in decor:
            img = pygame.image.load(f"assets/elements/{element["id"]}")
            img = pygame.transform.scale(img,element["taille"])
            self.window.blit(img,element["pos"])
        
    def draw(self, entities = [], decor = []):
        super().draw()
        self.draw_entity(entities)
        self.draw_decor(decor)