'''
Write a function, breadth_first_values, that takes in the root of binary tree. The function 
should return a list containing all values of the tree in breadth-first order

'''

from tree_node import Node
from collections import deque

def breadth_first_values(root): 
    if not root: 
        return []
    
    values = []
    queue = [root] 
    while queue: 
        current_node = queue.pop(0)
        values.append(current_node.val)

        if current_node.left: 
            queue.append(current_node.left)
        if current_node.right: 
            queue.append(current_node.right)
    return values


def breadth_first_values_v2(root): 
    if not root: 
        return []
    
    values = []
    queue = deque([root])
    while queue: 
        current_node = queue.popleft()
        values.append(current_node.val)

        if current_node.left: 
            queue.append(current_node.left)
        if current_node.right: 
            queue.append(current_node.right)
    return values



## Tests
a = Node ('a')
b = Node ('b')
c = Node ('c')
d = Node ('d')
e = Node ('e')
f = Node ('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f 

print(breadth_first_values_v2(a))


empty_node = None
print(breadth_first_values(empty_node))


