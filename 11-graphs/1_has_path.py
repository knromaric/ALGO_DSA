'''
    Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph and two nodes
    (srd, dst). The function should return a boolean indicating whether or not there exists a directed path between  the source and 
    destination 
'''
from collections import deque

# depth first approach
def has_path(graph, src, dst): 
    stack = [src]
    while stack: 
        current=stack.pop()
        if current== dst: 
            return True
        
        for neigbor in graph[current]: 
            stack.append(neigbor)
    
    return False

# breadth first approach
def has_path_bfa(graph, src, dst): 
    queue = deque([src])
    if queue: 
        current = queue.popleft()
        if current == dst: 
            return True 
        for neighbor in graph[current]: 
            queue.append(neighbor)
    
    return False 



def has_path_recursive(graph, src, dst): 
    if src==dst: 
        return True
    
    for neighbor in graph[src]: 
        if has_path(graph, neighbor, dst) == True: 
            return True
    return False

graph = {
    'f': ['g', 'i'], 
    'g': ['h'], 
    'h': [], 
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

print(has_path(graph, 'f', 'k'))
print(has_path_recursive(graph, 'f', 'k'))