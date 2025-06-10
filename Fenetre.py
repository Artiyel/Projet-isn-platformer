import pygame
import ctypes

pygame.init()


class Fenetre:
    ''''''
    def __init__(self, background, window):
        self.background = pygame.transform.scale(background, window.get_size())
        self.window = window
        #le décor 
        self.background = background

        #paramètre la fenêtre

        self.font = pygame.font.SysFont("New Times Roman", 40)
        # self.font = pygame.font.Font("assets/fonts/AncientModernTales-a7Po.ttf", 40)
        pygame.mixer.init()
        self.click = pygame.mixer.Sound("assets/sound/click.mp3")
        self.click_alt = pygame.mixer.Sound("assets/sound/click_effect.mp3")

        user32 = ctypes.windll.user32
        self.screensize = user32.GetSystemMetrics(0), int(user32.GetSystemMetrics(1)*0.93)

        self.background = pygame.transform.scale(self.background,self.screensize)


    def wrap_text(self, text, font, max_width):
        """Découpe le texte pour qu'il tienne dans max_width pixels."""
        words = text.split(' ')
        lines = []
        current_line = ""
        for word in words:
            test_line = current_line + word + " "
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + " "
        lines.append(current_line)
        return lines

    def draw(self):
        '''
        entrée : self
        sortie : None
        
        permet de créer l'affichage de la fenêtre
        '''
        self.window.blit(self.background,(0,0))
        #Faut mettre des trucs communs à tout les types de fenêtres

    def textbox(self,text):
        ''''''
        vol_red = 0.3
        pygame.mixer_music.set_volume(vol_red)
        running = True
        with open(text, 'r', encoding='utf-8') as f:
            for line in f:
                text_up = ""
                for char in line:
                    # Gestion des événements
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        if event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN):
                            running = False
                    if not running:
                        return  # On quitte proprement la fonction
                    if char != "$":
                        text_up += char
                        self.click.play()
                    if char == " ":
                        self.click_alt.play()
                    # Affichage avec retour à la ligne automatique
                    if text_up.strip() != "":
                        self.draw()  # Affiche le fond (image)
                        # Crée une surface semi-transparente pour la bande noire
                        rect_surface = pygame.Surface((self.screensize[0], self.screensize[1]//3), pygame.SRCALPHA)
                        rect_surface.fill((0, 0, 0, 180))  # 180 = transparence (0 transparent, 255 opaque)
                        self.window.blit(rect_surface, (0, int(self.screensize[1]*2/3)))
                        # Affichage du texte
                        lines = self.wrap_text(text_up, self.font, int(self.screensize[0]) - 40)
                        y = self.screensize[1]*2/3+50
                        for subline in lines:
                            textbox = self.font.render(subline, True, (255, 255, 255))
                            self.window.blit(textbox, (10, y))
                            y += self.font.get_height() + 5
                        pygame.display.flip()
                    pygame.time.delay(5)
                if not running:
                    return
                pygame.time.delay(500)
        self.window.blit(self.background, (0,0))
        while vol_red < 1 and running:
            vol_red += 0.1
            pygame.mixer_music.set_volume(vol_red)
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN):
                    running = False
        # Si l'utilisateur n'a pas quitté, attend un événement pour fermer
        if running:
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        waiting = False
                    if event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN):
                        waiting = False

    
    def run(self):
        '''
        Entrée : self
        Sortie : None

        Permet de lancer et faire tourner la fenêtre.
        '''
        print("run lancé")
        #initialisation de la fenêtre
        self.window.blit(self.background,(0,0))
        pygame.display.set_caption('Le jeu')
        #on affiche la fenêtre
        self.draw()

        self.running = True