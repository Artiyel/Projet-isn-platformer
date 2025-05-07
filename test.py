import pygame
from FenetreMenu import FenetreMenu
from FenetreJeu import FenetreJeu

import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

print(screensize)

#ça c'est pour la personne qui fera les controlleurs, ça permet d'afficher la fenêtre et de récupérer les actions.
#c'est principalement un fichier test donc feel free de le dégager du git

#on crée un objet fenêtre (note : c'est ici qu'on peut mettre en attribut le background et les bouttons si c'est un objet FenetreMenu)
win = FenetreMenu()
#On lance ça UNIQUEMENT pour initialiser la fenêtre, sinon c'est caca
win.run()

pygame.mixer_music.load("assets/music/Celeste_In_The_Mirror.mp3")
#la boucle principale
while win.running:
    if pygame.mixer_music.get_busy() == False:
        pygame.mixer_music.play()
    pygame.mixer_music.set_volume(1)
    #important de mettre du délai. Là on a une image tout les 20ms, donc 50fps.
    pygame.time.delay(20)
    #On utilise cette méthode pour afficher la fenêtre dans la boucle (interdiction d'utiliser .run() ici)
    win.draw()
    #Et voilà le job du controlleur. On récupère toutes les actions...
    for event in pygame.event.get():
        #... et on  exécute les trucs qu'on veut.
        if event.type == pygame.QUIT:
            win.running = False
            pygame.mixer_music.stop()
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_m]:
                win.textbox("assets/text/y0u.txt")
            if key[pygame.K_t]:
                win.textbox("assets/text/1t.txt")
            
    #NE PAS OUBLIER LE DISPLAY.FLIP() SINON CA VA FAIRE TOUT NOIR
    pygame.display.flip()