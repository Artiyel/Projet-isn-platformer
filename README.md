## Projet ISN 2025 - jeu de plateformes "ICI"

Composition du groupe :
BONNARD Martin ; 
PALMA Charlotte ; 
LE BOULAIRE Clément ; 
WATRIN Agathe.

Ce jeu s'appelle "ICI", et est de type "plateformer". Le but est de monter dans un décor 2D en sautant de plateforme en plateforme, jusqu'à arriver à la fin du niveau.
Le niveau finit quand an atteint cette plateforme finale, ou que l'on tombe dans le vide. Le joueur déplace son personnage grâce aux flèches directionnelles gauche et droite du clavier, et saute grâce à la flèche haut. L'affichage du jeu, trop petit pour afficher l'intégralité de la carte, suit le personnage dans ses mouvement en le gardant proche du centre de l'écran.
On peut à tout instant d'une partie revenir au menu grâce à la touche échap

Une fois le jeu lancé, plusieurs choix sont disponibles sur le menu : 
- Pour lancer une partie en mode noraml, il faut cliquer sur "Start Game". Le personnage du joueur se retrouve placé en bas à gauche d'un décor constitué de multiples plateformes, sur lesquelles il doit sauter pour se hisser jusqu'à la plateforme d'arrivée (différente des autres) en haut à droite.
- Le mode histoire n'est pas un jeu, mais un défilement de texte permettant de découvrir le contexte du jeu ; l'histoire d'ICI et les sentiments qui l'habitent.
- Le mode fantôme est semblable au mode normal, à un détail près : tandis que le joueur doit amener son personnage jusqu'à l'arrivée, il est poursuivi par une seconde entité à travers le décor. Si cette entité (que l'on appelle le "fantôme") vient à atteindre le joueur, la partie se termine.
  
Notre algorithme complexe est le fonctionnement du "fantôme", qui doit donc poursuivre le joueur à travers le décor en utilisant les mêmes actions de déplacement que le joueur. Cet algorithme fonctionne en plusieurs étapes:
- on convertit notre décor en quadrillage, puis en une matrice dont chaque coefficient indique si la case est occupée par une plateforme ou non
- à intervalle de temps réguliers, on marque la position du joueur et on en fait la destination du fantôme.
- On utilise des algorithmes de parcours de graphes et de dictionnaires pour déterminer les actions réalisables par le fantôme et définir le chemin qu'il parcourera pour relier sa destination.
- Le fantôme exécute ce chemin, et atteindra donc le joueur à moins qu'il ne le fuit.

Pour démarrer le jeu, il faut exécuter le fichier nommé "main.py", qui affiche le menu du jeu.

Précision : le module pygame est nécessaire pour le bon fonctionnement du jeu.
