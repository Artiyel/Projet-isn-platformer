mat = [[0,0,1,0,1,1],[1,1,0,0,1],[1,1,1,1,1]]
d_saut = 2 #nombre de case en y
d_dep = 1 #nombre de case en x
g = 1
vit = (d_dep,d_saut)

def atteignable(mat,posor,posar):
    #on regarde si on peut atteindre le sommet
    T = abs(2*vit[1]/g) #la durée du saut (x=x0 à t=0, x=x0 à t=T)
    res = False
    if (abs(posar[0]-posor[0]) <= d_dep*T and abs(posar[1]-posor[1]) < abs(g*(posar[0]-posor[0])/vit[0])) or (abs(posar[0]-posor[0]) < d_dep*T/2 and abs(posar[1]-posor[0]) < d_saut):
        res = True
    return res

def distance(pos1,pos2):
    #on assigne le coût du déplacement, à modifier, là c'est juste la distance
    return(((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)**(1/2))

arbre = {}
pos = [0,0]
#on crée un graphe
for ligne in mat:
    ''''''
    pos[0]=0
    for case in ligne:
        arbre[str(pos)]={}
        pos[0]+=1
    pos[1]+=1


#maintenant qu'on a toutes les coordonées dans le graphe, on crée les arrêtes
#on reviens sur chaque case
pos = [0,0]
for ligne in mat:
    pos[0]=0
    for case in ligne:
        pos2 = [0,0]
        #pour chaque case, on regarde si les autres cases sont atteignables et on leur assigne une distance
        for ligne in mat:
            pos2[0]=0
            for case in ligne:
                if atteignable(mat,pos,pos2):
                    arbre[str(pos)][str(pos2)] = distance(pos,pos2)
                pos2[0]+=1
            pos2[1]+=1
        pos[0]+=1
    pos[1]+=1

print(arbre)

