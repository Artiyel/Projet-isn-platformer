import pygame

class Button():
    def __init__(self, x, y, width,height, text='',text_color=(255,255,255),bg_color=(50,50,50), textsize = 10, font = pygame.font.Font("assets/fonts/AncientModernTales-a7Po.ttf"), sound = 'assets/sound/click_effect.mp3'):
        '''
        Entrée : paramêtres du bouton
        Sortie : None
        '''
        self.text_color = text_color
        self.bg_color = bg_color
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
        render = self.font.render(self.text, True, self.text_color)
        cadre = render.get_rect(center=(self.x + self.width//2, self.y + self.height//2))
        cadre.center = (self.x, self.y)
        win.blit(render,cadre)
        pygame.draw.rect(win, self.text_color, cadre.inflate(self.width,self.height),2,20)
    
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