'''SHORTEST PATH

    Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return  the length of the shortest path between A and B. Consider the length as teh number of edges in the path, not the number of nodes. If there is no path between A and B, then return -1

'''
from collections import deque


def shortest_path(edges, node_A, node_B): 
    graph = build_graph(edges)
    queue = deque([(node_A, 0)])
    visited = set([node_A])

    while queue: 
        current_node, distance = queue.popleft()
        
        if current_node == node_B: 
            return distance

        for neighbor in graph[current_node]: 
            if neighbor not in visited: 
                visited.add(neighbor)
                deque.append((neighbor, distance+1))

    return -1


def build_graph(edges): 
    graph = {}
    for a, b in edges: 
        if a not in graph:
            graph[a] = [] 
        if b not in graph: 
            graph[b] = []
        
        graph[a].append(b)
        graph[b].append(a)
    
    return graph



# tests 
edges = [
    ['w', 'x'], 
    ['x', 'y'], 
    ['z', 'y'], 
    ['z', 'v'], 
    ['w', 'v']
]

shortest_path(edges, 'w', 'z')