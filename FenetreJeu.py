from Fenetre import Fenetre
import pygame

class FenetreJeu(Fenetre):
    '''
    Gere l'affichage de 
    '''
    def __init__(self, background, window):
        super().__init__(background, window)

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
            if entity is not None:
                #img = pygame.image.load(f"assets/characters/{entity["id"]}")
                #img = pygame.transform.scale(img,entity["taille"])
                #self.window.blit(img,entity["pos"])
                rect = pygame.Rect(entity.x,entity.y,entity.x_taille,entity.y_taille)
                img = pygame.draw.rect(self.window,(255,255,255),rect)
            
    def draw_decor(self,decor):
        '''
        input :
            - self
            - decor :
                liste des éléments de décor sous la forme (WIP)
                
        Affiche les éléments du décor
        '''
        for element in decor:
            #img = pygame.image.load(f"assets/elements/{element["id"]}")
            #img = pygame.transform.scale(img,element["taille"])
            rect = pygame.Rect(element.x_pos,element.y_pos,element.x_taille,element.y_taille)
            if element.arrivee:
                img = pygame.draw.rect(self.window,(200,0,0),rect)
            else:
                img = pygame.draw.rect(self.window,(0,0,0),rect)

        
    def draw(self, entities = [], decor = []):
        #on dessine les éléments de base
        super().draw()
        #on affiche les entités
        self.draw_entity(entities)
        #on affiche les éléments de décor
        self.draw_decor(decor)