from functools import reduce
import queue

def get_undirected_graph(graph, start): 
    new_graph= dict() 
    queue_nodes= queue.Queue(len(graph))
    visited= set() 
    prev_nodes= dict() 
    prev_nodes[start]= None 
   
    new_graph[start]=(0,graph[start]) 
    visited.add(start)
    queue_nodes.put(start)

    while not queue_nodes.empty():
        node= queue_nodes.get()
        if node is not start:
            # heuristic= min(list(map(lambda x: x[0], prev_nodes[node])))+1 
            heuristic= prev_nodes[node][0]+1
            new_graph[node]=(heuristic, graph[node])
        for neighb in graph[node]:
            if neighb not in visited:
                visited.add(neighb)
                queue_nodes.put(neighb)
                # if neighb in prev_nodes:
                #     prev_nodes[neighb].append((new_graph[node][0],node))
                # else:
                prev_nodes[neighb]=(new_graph[node][0],node)
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




 




