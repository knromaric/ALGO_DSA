'''
 Write a function, tree_sum, that takes in the root of binary tree that contains number values.
 The function should return the total sum of all values in the tree.

'''


from tree_node import Node
from collections import deque


def sum_tree(root): 
    if not root: 
        return 0 
    
    queue = deque([root])
    total_sum = 0
    while queue: 
        current_node = queue.popleft()
        total_sum += current_node.val
        if current_node.left: 
            queue.append(current_node.left)
        if current_node.right: 
            queue.append(current_node.right)

    return total_sum 



def sum_tree_recursive(root): 
    if not root: 
        return 0
    return root.val + sum_tree_recursive(root.left) + sum_tree_recursive(root.right)  

## Tests
a = Node (3)
b = Node (11)
c = Node (4)
d = Node (4)
e = Node (-2)
f = Node (1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f 

print(sum_tree_recursive(a))
print(sum_tree(a))