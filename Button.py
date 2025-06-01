import pygame

class Button():
    def __init__(self, x, y, width,height, text='',text_color=(255,255,255),bg_color=(50,50,50), textsize = 30, font_name = "assets/fonts/AncientModernTales-a7Po.ttf", sound = 'assets/sound/click_effect.mp3'):
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
        self.font_name = font_name
        self.sound = pygame.mixer.Sound(sound)
        

    def draw(self,win):
        '''
        entrée : 
                self
                win : fenêtre sur laquelle on affiche le bouton
        sortie : None
        
        permet de dessiner le bouton
        '''
        # on crée la police avec la bonne taille
        font = pygame.font.Font(self.font_name, self.textsize)
        render = font.render(self.text, True, self.text_color)
        # on centre le texte dans le bouton
        cadre = render.get_rect(center=(self.x, self.y))
        # on crée le rectangle du bouton (centré sur self.x, self.y)
        rect = pygame.Rect(0, 0, self.width, self.height)
        rect.center = (self.x, self.y)
        # on dessine le fond du bouton (couleur unie)
        pygame.draw.rect(win, self.bg_color, rect, border_radius=10)
        # on dessine le texte par-dessus
        win.blit(render, cadre)
        rect_contour = pygame.Rect(0, 0, self.width + 2, self.height + 2)
        pygame.draw.rect(win, (255,255,255), rect, 2, border_radius=10)   # pour dessiner une bordure autour du bouton


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