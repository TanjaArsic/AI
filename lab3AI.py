from functools import reduce
import queue

def get_undirected_graph(graph, start): #breadth_first_search
    new_graph= dict() #value je tuple (heuristika,susedi)
    queue_nodes= queue.Queue(len(graph))
    visited= set() #pravi se skup da se oznace poseceni cvorovi
    prev_nodes= dict() #value je lista tupleova, prethodnici (heur,prethodnik)
    prev_nodes[start]= None #prvi cvor nema prethodnike

    new_graph[start]=(0,graph[start]) #heuristika za START je 0, susedi su D i H
    visited.add(start)
    queue_nodes.put(start)

    while not queue_nodes.empty():
        node= queue_nodes.get()
        #nadji minimum i dodaj u novi graf
        if node is not start:
            heuristic= min(list(map(lambda x: x[0], prev_nodes[node])))+1 #nalazi minimalnu heuristiku?
            new_graph[node]=(heuristic, graph[node])
        for neighbour in graph[node]: #dodaju se sledbenici
            if neighbour not in visited: #brzo je jer se koristi set 
                visited.add(neighbour)
                queue_nodes.put(neighbour)  
                prev_nodes[neighbour]=[(new_graph[node][0], node)] #tuple se kreira

                # print(prev_nodes[dest])

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




 




