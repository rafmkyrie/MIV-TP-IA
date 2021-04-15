
obst = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,2,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
    [1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,1,0,0,1,1,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,0,0,0,1,3,0,0,0,0,0,0,1,0,0,1],
    [1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]; 

w=512
h=512

ouvert = []
ferme = []
cout = 0

done = False
premiere_iteration = True
path_updated = False

def setup():
    size(w, h)
    tour=0
    
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
            
            if val == 0:
                r = 0
                g = 0
                b = 0
            elif val == 1:
                r = 0
                g = 0
                b = 255
            elif val == 2:
                r = 255
                g = 0
                b = 0
                
                if premiere_iteration:
                    x_init = i
                    y_init = j
            elif val == 3:
                r = 0
                g = 255
                b = 0
            elif val == 4:
                r = 100
                g = 100
                b = 100
            elif val == 5:
                r = 50
                g = 50
                b = 50
            elif val == 6:
                r = 255
                g = 255
                b = 0
            elif val == -1:
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
        if premiere_iteration:
            if obst[x_init][y_init] == 3:
                print("Found at (" + str(x_init) + ", " + str(y_init) +") !")
                done = True
            else:
                ouvert.append(((x_init, y_init),None))   
            premiere_iteration = False
        elif len(ouvert) == 0:
            print("Pas de chemin trouvé!")
            done = True
        else:
            largeur()
            cout += 1
    else:
        if path_updated:
            noLoop()
            return
        path = get_path()
        for step in path[:-2]:
            obst[step[0]][step[1]] = -1
        path_updated = True
            


def largeur():
    global done, cout

    current_pos = ouvert[0][0]
    current_x = current_pos[0]
    current_y = current_pos[1]
    
    #print(current_pos, obst[current_x][current_y], obst[current_x][current_y-1], obst[current_x+1][current_y], obst[current_x][current_y+1])
    
    # vérifier pixel de gauche
    exist = False
    for i in ferme+ouvert[1:]:
        if (current_x, current_y-1) == i[0]:
            exist = True
            break
            
    if not exist and not done:
        pix = obst[current_x][current_y-1]
        if pix == 0:
            ouvert.append(((current_x, current_y-1), current_pos))
            obst[current_x][current_y-1] = 5
        elif pix == 1:
            pass
        elif pix == 3:
            print("Found at (" + str(current_x) + ", " + str(current_y-1) +") !")
            print("Total moves : "+str(cout) + " moves.")
            obst[current_x][current_y-1] = 6
            done = True
            objectif_index = ((current_x, current_y-1), current_pos)
        else:
            print("Erreur pix gauche!")
        
    # vérifier pixel du bas
    exist = False
    for i in ferme+ouvert[1:]:
        if (current_x+1, current_y) == i[0]:
            exist = True
            break
            
    if not exist and not done:
        pix = obst[current_x+1][current_y]
        if pix == 0:
            ouvert.append(((current_x+1, current_y), current_pos))
            obst[current_x+1][current_y] = 5
        elif pix == 1:
            pass
        elif pix == 3:
            print("Found at (" + str(current_x+1) + ", " + str(current_y) +") !")
            print("Total moves : "+str(cout) + " moves.")
            obst[current_x+1][current_y] = 6
            done = True
            objectif_index = ((current_x+1, current_y), current_pos)
        else:
            print("Erreur pix bas!")
        
    # vérifier pixel de droite
    exist = False
    for i in ferme+ouvert[1:]:
        if (current_x, current_y+1) == i[0]:
            exist = True
            break
            
    if not exist and not done:
        pix = obst[current_x][current_y+1]
        if pix == 0:
            ouvert.append(((current_x, current_y+1), current_pos))
            obst[current_x][current_y+1] = 5
        elif pix == 1:
            pass
        elif pix == 3:
            print("Found at (" + str(current_x) + ", " + str(current_y+1) +") !")
            print("Total moves : "+str(cout) + " moves.")
            obst[current_x][current_y+1] = 6
            done = True
            objectif_index = ((current_x, current_y+1), current_pos)
        else:
            print("Erreur pix droite!", pix)
            
            
            
        # vérifier pixel du haut
    exist = False
    for i in ferme+ouvert[1:]:
        if (current_x-1, current_y) == i[0]:
            exist = True
            break
            
    if not exist and not done:
        pix = obst[current_x-1][current_y]
        if pix == 0:
            ouvert.append(((current_x-1, current_y), current_pos))
            obst[current_x-1][current_y] = 5
        elif pix == 1:
            pass
        elif pix == 3:
            print("Found at (" + str(current_x-1) + ", " + str(current_y) +") !")
            print("Total moves : "+str(cout) + " moves.")
            obst[current_x-1][current_y] = 6
            done = True
            objectif_index = ((current_x-1, current_y), current_pos)
        else:
            print("Erreur pix haut!", pix)    
            
        
    if not done:
        obst[current_x][current_y] = 4
    
    ferme.append(ouvert[0])
    del ouvert[0]
    
    if done:
        ferme.append(objectif_index)
    
    if len(ouvert) > 0 and not done:
        obst[ouvert[0][0][0]][ouvert[0][0][1]] = 2
        
        
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
            
    
            
            
            
            
            
            
            
