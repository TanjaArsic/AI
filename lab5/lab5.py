import copy
from pickle import FALSE
import queue

cur_map = []
stack = []
n = 4


def createTuple(x,y,number):
        if number!="*":
            polje=[x,y,int(number),[x for x in range(1,n+1)]]
        else:
            polje=[x,y,number,[x for x in range(1,n+1)]]
        return polje

def get_input():
    print("here")
    for i in range(n):
        cur_map.append([])
    for i in range(n):
        col = 0
        for j in input().split(" "):
            cur_map[i].append(createTuple(i,col,j))
            # popunjava se matrica i cell je self gore
            col = col +1   
            
def set_cell_num_domain(polje):
        x = polje[0]
        y = polje[1]
    # if polje[2]!= "*":
        for i in range(n):
            if i == x :
                continue
            try:
                cur_map[i][y][3].remove(polje[2])
                # ako negde dodje da nema opcija i da pritom nema vrednost vraca se false ...isto i za kolone
                if len(cur_map[i][y][3]) == 0 and cur_map[i][y][2]== "*":
                    return False
            except:
                pass 
        for j in range(n):
            if j == y: 
                continue
            try:
                cur_map[x][j][3].remove(polje[2])
                if len(cur_map[x][j][3]) == 0 and cur_map[x][j][2]== "*":
                    return False
            except:
                pass 
            

        return True


def set_map_domain():
    for i in range(n):
        for j in range(n):
            x = set_cell_num_domain(cur_map[i][j]) 
            # za svako neprazno polje izbacuje domene koji su suvisni..tj iz suseda izbacuje tu trenutnu brojku
    return x

def print_mrv():
    for i in range(n):
        for j in range(n):
            print(cur_map[i][j][3],end=",,,")
        print()
def brisiIzSuseda(element,polje,cur_map):
        for i in range(n):
                for domen in cur_map[polje[0]]:
                    if domen!=polje:
                        if element in  cur_map[polje[0]][i][3] :
                            cur_map[polje[0]][i][3].remove(element)
                        
                       
                for domen in cur_map[i][polje[1]]:
                    if cur_map[i][polje[1]]!=polje:
                        if element in  cur_map[i][polje[1]][3]:
                          cur_map[i][polje[1]][3].remove(element)   
def choose_element(polje):
    min=1000000
    element=-1
    for x in polje[3]:
        counter=0
        for i in range(n):
            
                for domen in cur_map[polje[0]][i][3]:
                    if cur_map[polje[0]][i][2]=="*":
                        if cur_map[polje[0]][i]!=polje:
                            if domen ==x:
                                counter+=1
                for domen in cur_map[i][polje[1]][3]:
                    if cur_map[i][polje[1]][2]=="*":
                        if cur_map[i][polje[1]]!=polje:
                            if domen ==x:
                                counter+=1
      
        if(min>counter):
            min=counter
            element=x

    print(element)  
    
    return element 

def forward_checking(cell):
    x = set_cell_num_domain(cell)
    if x == False:
        return "failuer"
# ako je broj domena u susedima 0,vraca false i mora da se vraca nazad i da uzima drugi broj 
    
# startni je prvi koji ima *
def depth_first_search(cur_map):
    i=0
    j=0
    start=[]
    print(cur_map)
    while i<4:
        while j<4:
            if cur_map[i][j][2]=="*":
                start=cur_map[i][j]
                j=4
                i=4
            else :
                j+=1
        j=0
        i+=1  
    
    stack_nodes = queue.LifoQueue()
    stack_nodes.put(start)
    stack.append(cur_map)
    while (not stack_nodes.empty()):
        polje = stack_nodes.get()
        if len(polje[3])==0:
            t="faileur"
        else:
            el=choose_element(polje)
            polje[2]=el
            polje[3].remove(el)
            bp_map = copy.deepcopy(cur_map)
            stack.append(bp_map)
            t = forward_checking(polje)
            
        if t != "failuer":
            pass
        else:
             print("back Track".center(40,"*"))
             cur_map = stack.pop()
            
        #for dest in graph[node]:
        for dest in reversed(cur_map[polje[0]]):
            if dest[2] =="*":
                # if dest not in visited:
                    # visited.add(dest)
                    stack_nodes.put(dest)
        for i in range(4):
                if cur_map[i][polje[1]][2] =="*":
                    # if dest not in visited:
                        #
                        stack_nodes.put(cur_map[i][polje[1]])
    for i in range(4):
            stringic=''
            for j in range(n):
             stringic+=str(cur_map[i][j][2])+" "
            print(stringic)
    
    

    

get_input() 
# unosimo matricu

set_map_domain()
# za svaki element matrice odredjujemo domen

depth_first_search(cur_map)