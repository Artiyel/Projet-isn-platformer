import pygame
import ctypes


pygame.init()


class Fenetre:
    ''''''
    def __init__(self, background):
        #le décor 
        self.background = background

        #paramètre la fenêtre

        self.font = pygame.font.Font(size=40)
        pygame.mixer.init()
        self.click = pygame.mixer.Sound("assets/sound/click.mp3")
        self.click_alt = pygame.mixer.Sound("assets/sound/click_effect.mp3")

        user32 = ctypes.windll.user32
        self.screensize = user32.GetSystemMetrics(0) , user32.GetSystemMetrics(1)*0.93

        self.background = pygame.transform.scale(self.background,self.screensize)

    def draw(self):
        '''
        entrée : self
        sortie : None
        
        permet de créer l'affichage de la fenêtre
        '''
        #Faut mettre des trucs communs à tout les types de fenêtres

    def textbox(self,text):
        ''''''
        vol_red = 0.3
        pygame.mixer_music.set_volume(vol_red)
        with open(text,'r', encoding='utf-8') as f:
            for line in f:
                text_up = ""
                for char in line:
                    if char != "$":
                        text_up +=char
                        self.click.play()
                    if char == " ":
                        self.click_alt.play()
                    rect = pygame.Rect(0,self.screensize[1]*2/3,self.screensize[0],self.screensize[1]/3)
                    pygame.draw.rect(self.window,(0,0,0),rect)
                    textbox = self.font.render(text_up, True, (255, 255, 255))
                    self.window.blit(textbox,(10,self.screensize[1]*2/3+50))
                    pygame.display.flip()
                    pygame.time.delay(30)
                pygame.time.delay(500)
        self.window.blit(self.background,(0,0)) 
        while vol_red<1:
                    vol_red+=0.1
                    pygame.mixer_music.set_volume(vol_red)
                    pygame.time.delay(50)

    
    def run(self):
        '''
        Entrée : self
        Sortie : None

        Permet de lancer et faire tourner la fenêtre.
        '''
        #initialisation de la fenêtre
        self.window = pygame.display.set_mode((self.screensize))
        self.window.blit(self.background,(0,0))
        pygame.display.set_caption('Le jeu')
        #on affiche la fenêtre
        self.draw()

        self.running = True