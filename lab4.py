# Dat je skup domina u kome najveća ima dve četvorke na polovinama i ima ih ukupno 15. Igrač u
# svakom koraku postavlja jednu dominu na jedan od krajeva poštujući pravila igre domina.
# Poređati sve domine iz ovog skupa u niz poštujući pravila igre domina tako da se i dve domine na
# krajevima mogu uklopiti poštujući pravila igre domina. Zapamtiti korake pravljenja niza kojim se
# došlo do rešenja.

import time
import math

def generateDominoes(max):
    retlist=[]
    for i in range(0,max+1):
        for j in range (i,max+1):
            retlist.append((i,j))
    return tuple(retlist) 

def heuristics(placed, available):
    if(len(available)==0):
        return -math.inf
    left=placed[0][0]
    right=placed[-1][-1]
    possible_left=0
    possible_right=0
    for dominoe in available:
        if (dominoe[0]==right or dominoe[-1]==right):
            possible_right+=1
        if (dominoe[-1]==left or dominoe[0]==left):
            possible_left+=1
    if((possible_left+possible_right)==0):
        return math.inf
    if(len(available)-1==0):
        return -100000
    return 2000*(len(available)-1) + (possible_left+possible_right)*1 

def possible_placement(placed, remaining): 
    left=placed[0][0]
    right=placed[-1][-1]
    retlist=[]
    for dominoe in remaining:
        if (dominoe[0]==right):
            l=list(placed)
            l.append(dominoe)
            t=tuple(l)
            retlist.append(t)
        if (dominoe[0]==left and (dominoe[0]!=dominoe[-1])):
            l=list(placed)
            l.insert(0,dominoe[::-1])
            t=tuple(l)
            retlist.append(t)
        if (dominoe[-1]==left):
            l=list(placed)
            l.insert(0,dominoe)
            t=tuple(l)
            retlist.append(t)
        if (dominoe[-1]==right and (dominoe[0]!=dominoe[-1])):
            l=list(placed)
            l.append(dominoe[::-1])
            t=tuple(l)
            retlist.append(t)
    return retlist

def init_dominoe(open_set,g,prev_nodes,available): 
    for dominoe in available:
        node=(dominoe,)
        open_set.add(node) 
        g[node] = 0
        prev_nodes[node] = None 

def astar(available):
    found_end = False
    open_set = set()
    closed_set = set()
    final = tuple()
    g = {}
    prev_nodes = {}
    init_dominoe(open_set,g,prev_nodes,available)
    while len(open_set) > 0 and (not found_end): 
        node = None 
        for next_node in open_set:
            if node is None:
                node = next_node 
            # elif(len(next_node) == len(available)):
            #     node = next_node
            #     break
            else:
                fcurr=g[node] + heuristics(node,[x for x in available if x not in node and x[::-1] not in node])
                fnext=g[next_node] + heuristics(next_node,[x for x in available if x not in next_node and x[::-1] not in next_node])
                if( fnext < fcurr ): 
                    node = next_node #
        if len(node) == len(available):
            found_end = True
            final = node
            break
        for m in possible_placement(node,[x for x in available if x not in node and x[::-1] not in node]): 
            if m not in open_set and m not in closed_set: 
                open_set.add(m)
                prev_nodes[m] = node
                g[m] = g[node] + 1000
            else:
                if g[m] > g[node] + 1000:
                    g[m] = g[node] + 1000
                    prev_nodes[m] = node
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)
        open_set.remove(node)
        closed_set.add(node)
    path = []
    if found_end:
        prev = final
        while prev_nodes[prev] is not None: 
            path.append(prev)
            prev = prev_nodes[prev] 
        path.append(prev)
        path.reverse() 
    return path

start=time.time()
for step in astar(generateDominoes(4)):
    print(step)
end=time.time()
print(end-start)