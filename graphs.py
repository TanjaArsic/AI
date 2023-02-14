

import queue


def ObradiJedan(graph,node1,H):
    queue_nodes = queue.Queue(len(graph))
    visited = set()
    H[node1]=0 #ciljni cvor ima heuristiku 0
    queue_nodes.put(node1)
    while not queue_nodes.empty():
        el=queue_nodes.get()
        visited.add(el)
        for e in graph[el]: #za sve neposecene susede cvora proveravamo heuristiku
            if e not in visited: 
                queue_nodes.put(e)
                if e not in H.keys(): #ova provera mora da postoji zbog prvog obilaska
                    H[e]=H[el]+1      # ne moze odmah if H[e]>H[el]+1 ako ne postoji H[e]
                else:
                    if H[e]>H[el]+1: #ako je nova procena manja od postojece menjamo
                        H[e]=H[el]+1
                

def DvojnaHeuristika(graph,node1,node2):
    H=dict() #heuristika je dictionary koji za key node ima value njegovu heuristiku
    ObradiJedan(graph,node1,H)
    ObradiJedan(graph,node2,H)
    g2=dict(map(lambda x:(x,(H[x],graph[x])),graph)) #pravi se graf sa heuristikom
    return g2 # u formatu je npr 'A':(3,['B','C','D']) gde je 3 H['A']


graph = {
'A' : ['B','C'],
'B' : ['A', 'D', 'E'],
'C' : ['A', 'F', 'G'],
'D' : ['B','H'],
'E' : ['B', 'G', 'I'],
'F' : ['C', 'J'],
'G' : ['C','E','J'],
'H' : ['D'],
'I' : ['E','J'],
'J' : ['F','G','I']
}

HGraf=DvojnaHeuristika(graph,'A','E')
print(HGraf)


