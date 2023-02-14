from functools import reduce
import queue

def get_undirected_graph(graph, start): #breadth_first_search
    new_graph= dict() #value je tuple (heuristika,susedi)
    queue_nodes= queue.Queue(len(graph))
    visited= set() #pravi se skup da se oznace poseceni cvorovi
    prev_nodes= dict() #value je lista tupleova, prethodnici (heur,prethodnik)
    prev_nodes[start]= None #prvi cvor nema prethodnike
    done_nodes=list()

    done_nodes.append(start)
    new_graph[start]=(0,graph[start]) #heuristika za START je 0, susedi su D i H
    visited.add(start)
    queue_nodes.put(start)

    while not queue_nodes.empty():
        node= queue_nodes.get()
        #nadji minimum i dodaj u novi graf
        if node is not start:
            heuristic= min(list(map(lambda x: x[0], prev_nodes[node])))+1 #nalazi minimalnu heuristiku?
            new_graph[node]=(heuristic, graph[node])
        for neighb in graph[node]:
            if neighb not in visited:
                visited.add(neighb)
                queue_nodes.put(neighb)
                
            if neighb not in done_nodes:#nije moralo, ali da se ne bi dodavali susedi i nakon sto se cvor obradi
                if neighb in prev_nodes:
                    prev_nodes[neighb].append((new_graph[node][0],node))
                else:
                    prev_nodes[neighb]=[(new_graph[node][0],node)]   
    return new_graph


graph= { 
'A': ['B','C'],
'B': ['A','D', 'E'],
'C': ['A','F', 'G'],
'D': ['B','H'],
'E': ['B','G', 'I'],
'F': ['C','J'],
'G': ['E','C','J'],
'H': ['D'],
'I': ['E','J'],
'J': ['I','G','F']
}

graph2= { 
'A': ['B','C','D'],
'B': ['A', 'C', 'E', 'F'],
'C': ['A','F', 'B'],
'D': ['A','G','H'],
'E': ['B','F'],
'F': ['C','E'],
'G': ['D','H'],
'H': ['D','G']
}

graph3= { 
'A': []
}


# novi3= breadth_first_search(graph3, 'A')
novi2= get_undirected_graph(graph2, 'G')
# novi= breadth_first_search(graph, 'A')
print(novi2)




 




