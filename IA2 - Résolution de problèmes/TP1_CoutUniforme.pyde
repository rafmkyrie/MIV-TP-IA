
obst = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
    [1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,1,0,0,1,1,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
    [1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,3,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]; 

w=512
h=512

# Costs
COST_UP = 6
COST_DOWN = 5
COST_RIGHT = 8
COST_LEFT = 12

ouvert = []
ferme = []

done = False
premiere_iteration = True
path_updated = False

def setup():
    size(w, h)
    tour=0
    
def choisir_noeud():
    liste = sorted(ouvert, key=lambda tup: tup[2])
    return liste[0]
    
    
def draw():    
    global done, premiere_iteration, cout, path_updated
    
       
    out = createImage(w,h,RGB)
    out.loadPixels()
    for x in range(w):
        for y in range(h):
            loc = x + y*w
            stepx = w/16
            stepy = h/16
            i = y / stepy 
            j = x / stepx
            val = obst[i][j]
            
            if val == 0:  # noir    - sol -
                r = 0
                g = 0
                b = 0
            elif val == 1:  # bleu    - obstacle -
                r = 0
                g = 0
                b = 255
            elif val == 2: # rouge   - robot -
                r = 255
                g = 0
                b = 0
                
                if premiere_iteration:
                    x_init = i
                    y_init = j
            elif val == 3:  # vert    - objectif -
                r = 0
                g = 255
                b = 0
            elif val == 4:   # gris clair  - noeud traité -
                r = 100
                g = 100
                b = 100
            elif val == 5:   # gris foncé  - noeud déjà passé -
                r = 50
                g = 50
                b = 50
            elif val == 6:   # jaune  - objectif trouvé -
                r = 255
                g = 255
                b = 0
            elif val == -1:  # rose   - path -
                r = 255
                g = 166 
                b = 221
            else:
                print("error val")
                
            c = color(r,g,b)
            out.pixels[loc] = c
    out.updatePixels()
    image(out, 0, 0)


    if not done:
        
        # vérifier si le noeud de début n'est pas l'objectif
        if premiere_iteration:
            ouvert.append(((x_init, y_init),None, 0))   
            premiere_iteration = False

        elif len(ouvert) == 0:
            print("Pas de chemin trouvé!")
            done = True

        else:
            cout_uniforme()
    else:
        if path_updated:
            noLoop()
            return
        path = get_path()
        for step in path[:-1]:
            obst[step[0]][step[1]] = -1
        path_updated = True
        
        
        

def cout_uniforme():
    global done
    
    if len(ferme):
        obst[ferme[-1][0][0]][ferme[-1][0][1]] = 5

    current_pos = choisir_noeud()
    current_x = current_pos[0][0]
    current_y = current_pos[0][1]
    
    #print(current_pos[0])
    #print(obst[current_x][current_y])
    
    #print(current_pos, obst[current_x][current_y], obst[current_x][current_y-1], obst[current_x+1][current_y], obst[current_x][current_y+1])
    
    # Vérification de si noeud actuel == objectif
    if obst[current_x][current_y] == 3:
        # noeud actuel == objectif
         
        print("Found at (" + str(current_x) + ", " + str(current_y) +") !")
        print("Total cost : "+str(current_pos[2]))
        obst[current_x][current_y] = 6
        done = True
        objectif_index = ((current_x, current_y), current_pos)
         
    else:
        # noeud actuel != objectif
        
        # Traitement du noeud du haut
        exist = False
        
        if obst[current_x-1][current_y] == 1:
            exist = True
            
        if not exist:
            for i in ferme:
                if i[0] == (current_x-1, current_y):
                    exist = True
                
        if not exist:
            for i in ouvert:
                if i[0] == (current_x-1, current_y):
                    exist = True
                    if i[2] > current_pos[2] + COST_UP:
                        i[2] = current_pos[2] + COST_UP       # Mise à jour du coût
                        i[1] = current_pos[0]                 # Mise à jour du père
                    break
            
        if not exist:
            ouvert.append(tuple([(current_x-1, current_y), current_pos[0], current_pos[2] + COST_UP]))
            
            
            
        # Traitement du noeud du bas
        exist = False
        
        if obst[current_x+1][current_y] == 1:
            exist = True
            
        if not exist:
            for i in ferme:
                if i[0] == (current_x+1, current_y):
                    exist = True
        
        if not exist:
            for i in ouvert:
                if i[0] == (current_x+1, current_y):
                    exist = True
                    if i[2] > current_pos[2] + COST_DOWN:
                        i[2] = current_pos[2] + COST_DOWN     # Mise à jour du coût
                        i[1] = current_pos[0]                 # Mise à jour du père
                    break
            
        if not exist:
            ouvert.append(tuple([(current_x+1, current_y), current_pos[0], current_pos[2] + COST_DOWN]))
            
            
        # Traitement du noeud de droite
        exist = False
        
        if obst[current_x][current_y+1] == 1:
            exist = True
            
        if not exist:
            for i in ferme:
                if i[0] == (current_x, current_y+1):
                    exist = True
        
        if not exist:
            for i in ouvert:
                if i[0] == (current_x, current_y+1):
                    exist = True
                    if i[2] > current_pos[2] + COST_RIGHT:
                        i[2] = current_pos[2] + COST_RIGHT       # Mise à jour du coût
                        i[1] = current_pos[0]                 # Mise à jour du père
                    break
            
        if not exist:
            ouvert.append(tuple([(current_x, current_y+1), current_pos[0], current_pos[2] + COST_RIGHT]))
            
        
        
        # Traitement du noeud de gauche
        exist = False
        
        if obst[current_x][current_y-1] == 1:
            exist = True
            
        if not exist:
            for i in ferme:
                if i[0] == (current_x, current_y-1):
                    exist = True
        
        if not exist:
            for i in ouvert:
                if i[0] == (current_x, current_y-1):
                    exist = True
                    if i[2] > current_pos[2] + COST_LEFT:
                        i[2] = current_pos[2] + COST_LEFT      # Mise à jour du coût
                        i[1] = current_pos[0]                 # Mise à jour du père
                    break
            
        if not exist:
            ouvert.append(tuple([(current_x, current_y-1), current_pos[0], current_pos[2] + COST_LEFT]))
            
    # Ajout du noeud actuel à la liste Ferme
    ferme.append(current_pos)        
    
    # Suppression du noeud actuel de la liste Ouvert
    for i in ouvert:
        if i[0] == current_pos[0]:
            ouvert.remove(i)
        
    obst[current_x][current_y] = 2

        
        
def get_path():
    path = []
    pos = ferme[-1]
    child = ferme[-1][0]
    parent = ferme[-1][1]
    i = -1
    
    while ferme[i][1] != None:
        if ferme[i][0] == child:
            path.append(ferme[i][0])
            child = ferme[i][1]
            i-=1
        else:
            i-=1
            
    path.append(ferme[0][0])
    path = path[::-1]
    
    print("Path : ")
    print(path)
    
    return path
            
    
            
            
            
            
            
            
            
