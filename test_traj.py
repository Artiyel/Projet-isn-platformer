###----------------------------------------------------------------------------------------------###
#ces variables sont là pour le test, elles existent déjà sous d'autres formes dans le reste du code

mat = [[0,0,1,0,1,1],[1,1,0,0,1],[1,1,1,1,1]]
d_saut = 2 #nombre de case en y
d_dep = 1 #nombre de case en x
g = 1 #constante pour l'accéleration de la gravité
vit = (d_dep,d_saut)

###----------------------------------------------------------------------------------------------###

def atteignable(pos_origine,pos_arrivee):
    '''
    entrée :
        - pos_origine : liste [x_origine, y_origine]
        - pos_arrivee : liste [x_arrivee, y_arrivee]

    sortie : bool

    vérifie que le déplacement de A vers B est possible avec les mouvements du personnage (renvoie True)
    '''
    #on regarde si on peut atteindre le sommet
    T = abs(2*vit[1]/g) #la durée du saut (x=x0 à t=0, x=x0 à t=T)
    res = False #ca c'est ce qu'on va renvoyer
    if (abs(pos_arrivee[0]-pos_origine[0]) <= vit[0]*T and abs(pos_arrivee[1]-pos_origine[1]) < abs(g*(pos_arrivee[0]-pos_origine[0])/vit[0])) or (abs(pos_arrivee[0]-pos_origine[0]) < vit[0]*T/2 and abs(pos_arrivee[1]-pos_origine[0]) < vit[1]):
        res = True #tkt ça marche
    return res

def distance(pos1,pos2):
    """
    entrée : 
        - pos1 = [x1,y1] et pos2 = [x2,y2]

    sortie :
        - valeur représentant le coût du déplacement (pour l'instant = distance, remplacer par temps dans le code principal)
    """
    #on assigne le coût du déplacement, à modifier, là c'est juste la distance
    return(((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)**(1/2))

graphe = {} #le graphe de tout les chemins
pos = [0,0] #on initialise pos
#on crée un graphe
for ligne in mat:#pour tout les y
    ''''''
    pos[0]=0 #on se place en x = 0
    for case in ligne: #pour tout les x
        #on regarde si c'est une plateforme ou du vide
        if case == 1:
            #si c'est une plateforme on l'ajoute au graphe
            graphe[str(pos)]={}
        pos[0]+=1
    pos[1]+=1


#maintenant qu'on a toutes les coordonées dans le graphe, on crée les arrêtes

#on reviens sur chaque case (plateformes)
for case1 in graphe:
    #on redécompose la position (la clé doit être un str et on a besoin d'une liste)
    pos1 = [int(x) for x in case1.strip("[]").split(",")]

    #pour chaque case, on regarde si les autres cases sont atteignables et on leur assigne un coût
    for case2 in graphe:
        pos2 = [int(x) for x in case2.strip("[]").split(",")]
        if atteignable(pos1,pos2):
            graphe[case1][case2] = distance(pos,pos2)


print(graphe)
print(graphe.keys())

