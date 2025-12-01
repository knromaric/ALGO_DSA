
from collections import deque

def depth_first_print(graph, start):
    stack = [start]
    while stack: 
        current = stack[-1]
        print(current, end=" -> ")
        current = stack.pop()
        for neigbor in graph[current]: 
            stack.append(neigbor)

def depth_first_print_recursive(graph, start): 
    print(start, end=" -> ")
    for neighbor in graph[start]: 
        depth_first_print_recursive(graph, neighbor)
    

def breadth_first_print(graph, start):
    queue = deque([start])
    while queue: 
        current = queue[0]
        print(current, end=" -> ")
        current = queue.popleft()
        for neigbor in graph[current]: 
            queue.append(neigbor)



graph = {
    "a" : ["b", "c"], 
    "b" : ["d"],
    "c" : ["e"],
    "d" : ["f"], 
    "e" : [], 
    "f" : []
}


print("depth first method ----------------------------------")
depth_first_print(graph, "a")
print()
depth_first_print_recursive(graph, "a")


print()
print("Breadth first method ----------------------------------")
breadth_first_print(graph, "a")
# print()
# depth_first_print_recursive(graph, "a")