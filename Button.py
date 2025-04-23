import pygame

class Button():
    def __init__(self, img, x, y, width,height, text='', textsize = 10, font = None, sound = 'assets/sound/click_effect.mp3'):
        '''
        Entrée : paramêtres du bouton
        Sortie : None
        '''
        if type(img) == tuple:
            self.color = img
        self.x = x 
        self.y = y 
        self.width = width
        self.height = height
        self.text = text
        self.textsize = textsize
        self.font = font
        self.sound = pygame.mixer.Sound(sound)
        

    def draw(self,win):
        '''
        entrée : 
                self
                win : fenêtre sur laquelle on affiche le bouton
        sortie : None
        
        permet de dessiner le bouton
        '''
        render = self.font.render(self.text, True, self.color)
        cadre = render.get_rect()
        cadre.center = (self.x, self.y)
        win.blit(render,cadre)
        pygame.draw.rect(win, self.color, cadre.inflate(self.width,self.height),2,20)
    
    def is_hit(self):
        '''
        entrée : self
        sortie : reponse : Booléen
                    renvoie True si le curseur est sur le bouton, False sinon
        '''
        reponse = False
        if (
            self.x - self.width < pygame.mouse.get_pos()[0]
            and self.x + self.width > pygame.mouse.get_pos()[0]
            and self.y - self.height < pygame.mouse.get_pos()[1]
            and self.y + self.height > pygame.mouse.get_pos()[1]
            ):
            reponse = True
            pygame.mixer.Channel(1).play(self.sound)
        return reponse