import heapq

class Graphe :

    def __init__(self, controleur):
        self.controleur = controleur
        self.matrice = controleur.matrice
        self.taille_case = controleur.taille_case
        self.creer_graphe()
        
    def atteignable(self,pos_origine,pos_arrivee):
        '''
        entrée :
            - pos_origine : liste [x_origine, y_origine]
            - pos_arrivee : liste [x_arrivee, y_arrivee]

        sortie : bool

        vérifie que le déplacement de A vers B est possible avec les mouvements du personnage (renvoie True)
        '''
        g = 4/self.taille_case
        v_saut = -65/self.taille_case
        v_dep = self.controleur.perso.vitesse_marche
        #on regarde si on peut atteindre le sommet
        T = abs(2*v_saut/g) #la durée du saut (x=x0 à t=0, x=x0 à t=T)
        res = False #ca c'est ce qu'on va renvoyer
        print(pos_arrivee[0]-pos_origine[0])
        print(v_dep*T)
        print(".")
        print(pos_arrivee[1]-pos_origine[1])
        print(g*(pos_arrivee[0]-pos_origine[0])/v_dep)
        print(".")
        if (abs(pos_arrivee[0]-pos_origine[0]) <= v_dep*T and pos_origine[1]-pos_arrivee[1] < abs(g*(pos_arrivee[0]-pos_origine[0])/v_dep)) or (abs(pos_arrivee[0]-pos_origine[0]) < v_dep*T/2 and pos_arrivee[1]-pos_origine[0] < v_saut):
            res = True #tkt ça marche
        return res

    def distance(self,pos1,pos2):
        """
        entrée : 
            - pos1 = [x1,y1] et pos2 = [x2,y2]

        sortie :
            - valeur représentant le coût du déplacement (pour l'instant = distance, remplacer par temps dans le code principal)
        """
        #on assigne le coût du déplacement, à modifier, là c'est juste la distance
        return(((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)**(1/2))

    def creer_graphe(self):
        self.graphe = {} #le graphe de tout les chemins
        pos = [0,0] #on initialise pos
        #on crée un graphe
        for ligne in self.matrice:#pour tout les y
            ''''''
            pos[0]=0 #on se place en x = 0
            for case in ligne: #pour tout les x
                #on regarde si c'est une plateforme ou du vide
                if case == 1:
                    #si c'est une plateforme on l'ajoute au graphe
                    self.graphe[str(pos)]={}
                pos[0]+=1
            pos[1]+=1
            #maintenant qu'on a toutes les coordonées dans le graphe, on crée les arrêtes

        #on reviens sur chaque case (plateformes)
        for case1 in self.graphe:
            #on redécompose la position (la clé doit être un str et on a besoin d'une liste)
            pos1 = [int(x) for x in case1.strip("[]").split(",")]

            #pour chaque case, on regarde si les autres cases sont atteignables et on leur assigne un coût
            for case2 in self.graphe:
                pos2 = [int(x) for x in case2.strip("[]").split(",")]
                if self.atteignable(pos1,pos2):
                    self.graphe[case1][case2] = self.distance(pos1,pos2)
    
    def trouver_chemin(self, pos1):
        if pos1 in self.graphe.keys():
            #init
            dist = {sommet : float("inf") for sommet in self.graphe}
            dist["pos1"] = 0

            attente = [(0,str(pos1))]
            heapq.heapify(attente)

            visites = set()

            while attente:
                dist_act, sommet_act = heapq.heappop(attente)
                if sommet_act in visites:
                    continue
                visites.add(sommet_act)

                for voisin, cout in self.graphe[sommet_act].items():
                    test_dist = dist_act + cout
                    if test_dist < dist[voisin]:
                        dist[voisin] = test_dist
                        heapq.heappush(attente,(test_dist,voisin))

            pred = {sommet : None for sommet in self.graphe}
            for sommet,distance in dist.items():
                for voisin, cout in self.graphe[sommet].items():
                    if dist[voisin] == distance + cout:
                        pred[voisin] = sommet
            return dist,pred
        
    def chemin_le_plus_court(self, origin : str, arivee : str):
        _,pred = self.trouver_chemin(origin)

        chemin = []
        sommet_act = arivee

        while sommet_act:
            chemin.append(sommet_act)
            sommet_act = pred[sommet_act]

            chemin.reverse()
        return chemin

