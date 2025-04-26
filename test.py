import pygame
from FenetreMenu import FenetreMenu
from FenetreJeu import FenetreJeu

#ça c'est pour la personne qui fera les controlleurs, ça permet d'afficher la fenêtre et de récupérer les actions.
#c'est principalement un fichier test donc feel free de le dégager du git

#on crée un objet fenêtre (note : c'est ici qu'on peut mettre en attribut le background et les bouttons si c'est un objet FenetreMenu)
win = FenetreMenu()
#On lance ça UNIQUEMENT pour initialiser la fenêtre, sinon c'est caca
win.run()
#la boucle principale
while win.running:
    #important de mettre du délai. Là on a une image tout les 20ms, donc 50fps.
    pygame.time.delay(20)
    #On utilise cette méthode pour afficher la fenêtre dans la boucle (interdiction d'utiliser .run() ici)
    win.draw()
    #Et voilà le job du controlleur. On récupère toutes les actions...
    for event in pygame.event.get():
        #... et on  exécute les trucs qu'on veut.
        if event.type == pygame.QUIT:
            win.running = False
            
    #NE PAS OUBLIER LE DISPLAY.FLIP() SINON CA VA FAIRE TOUT NOIR
    pygame.display.flip()