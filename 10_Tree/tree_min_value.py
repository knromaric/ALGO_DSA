'''
Write a function, tree_min_value, that takes in the root of a binary tree that contains number
values. The function should return the minimum value within the tree

you may assume that the input tree is non-empty

'''



from math import inf
from tree_node import Node

def tree_min_value(root): 
    '''
    we solve this problem using depth-first order
    '''
    stack = [root]
    min = float("inf")
    while stack: 
        current_node = stack.pop()
        if current_node.val < min: 
            min = current_node.val
        if current_node.left: 
            stack.append(current_node.left)
        if current_node.right: 
            stack.append(current_node.right)
    return min 




def tree_min_value_recursive(root): 
    if not root: 
        return float("inf")
    min_left = tree_min_value_recursive(root.left)
    min_right = tree_min_value_recursive(root.right)
    return min(root.val, min_left, min_right)







## Tests
a = Node (5)
b = Node (11)
c = Node (3)
d = Node (4)
e = Node (2)
f = Node (1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f 

empty_node = None
print(tree_min_value_recursive(a))
print(tree_min_value(a))