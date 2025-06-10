## Projet ISN 2025 - jeu de plateformes "ICI"

Composition du groupe :
BONNARD Martin ; 
PALMA Charlotte ; 
LE BOULAIRE Clément ; 
WATRIN Agathe.

Notre projet consiste en le développement et la programmation en python d'un jeu, qui utilisera une interface graphique et répondra à des commandes du joueur.\
Ce jeu s'appelle "ICI", et est de type "plateformer". Le but est de monter dans un décor 2D en sautant de plateforme en plateforme, jusqu'à arriver à la fin du niveau.
Le niveau finit quand an atteint cette plateforme finale, ou que l'on tombe dans le vide. Le joueur déplace son personnage grâce aux flèches directionnelles gauche et droite du clavier, et saute grâce à la flèche haut.\
L'affichage du jeu, trop petit pour afficher l'intégralité de la carte, suit le personnage dans ses mouvement en le gardant proche du centre de l'écran.
On peut à tout instant d'une partie revenir au menu grâce à la touche échap

Une fois le jeu lancé, plusieurs choix sont disponibles sur le menu : 
- Pour lancer une partie en mode normal, il faut cliquer sur "Start Game". Le personnage du joueur se retrouve placé en bas à gauche d'un décor constitué de multiples plateformes, sur lesquelles il doit sauter pour se hisser jusqu'à la plateforme d'arrivée (différente des autres) en haut à droite.
- Le mode histoire n'est pas un jeu, mais un défilement de texte permettant de découvrir le contexte du jeu ; l'histoire d'ICI et les sentiments qui l'habitent.
  Ce texte est importé d'un fichier .txt et affiché par morceau à l'écran.
- Le mode fantôme est semblable au mode normal, à un détail près : tandis que le joueur doit amener son personnage jusqu'à l'arrivée, il est poursuivi par une seconde entité à travers le décor. Si cette entité (que l'on appelle le "fantôme") vient à atteindre le joueur, la partie se termine.

Notre programme utilise donc plusieurs fichiers importés (rassemblés et triés dans le dossier "assets") ; des images pour la cosmétique de l'interface graphique, une musique pour l'ambiance du jeu, des sons pour le bruit des clicks, et des fichiers texte pour afficher l'histoire de l'univers du jeu à plusieurs moments du jeu et dans le mode Histoire.
  
Notre algorithme complexe est le fonctionnement du "fantôme", qui doit donc poursuivre le joueur à travers le décor en utilisant les mêmes actions de déplacement que le joueur. Cet algorithme fonctionne en plusieurs étapes:
- on convertit notre décor en quadrillage, puis en une matrice dont chaque coefficient indique si la case est occupée par une plateforme ou non
- à intervalle de temps réguliers, on marque la position du joueur et on en fait la destination du fantôme.
- On utilise des algorithmes de parcours de graphes et de dictionnaires pour déterminer les actions réalisables par le fantôme et définir le chemin qu'il parcourera pour relier sa destination.
- Le fantôme exécute ce chemin, et atteindra donc le joueur à moins qu'il ne le fuit.

Pour démarrer le jeu, il faut exécuter le fichier nommé "main.py", qui affiche le menu du jeu.

Les modules pygame, time sont nécessaires pour le bon fonctionnement du jeu.\
Nous avons utilisé pour le développement de ce jeu un format de projet GitHub, afin de rassembler tous les fichiers de code, de cosmétique et de texte. Cette méthode permet également à chaque membre du groupe de travailler sur une partie du code depuis son poste personnel. Entre chaque rencontre et mise au point du groupe, chacun avait donc des tâches à effectuer de son côté, qui n'affectaient pas le code commun jusqu'au "push" sur le GitHub.\
Nous n'avons pas utilisé de code généré par IA.
