''' Max Root to Leaf Path Sum

    Write a function, max_path_sum, that takes in the root of a binary tree that contains number values.
    The function should return the maximum sum of any root to leaf path within the tree.

'''

from tree_node import Node


def max_root_to_leaf_path(root): 
    if not root: 
        return -float('inf')
    if not root.left and not root.right: 
        return root.val
    
    left_val = max_root_to_leaf_path(root.left)
    right_val = max_root_to_leaf_path(root.right)
    return root.val + max(left_val, right_val)




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


print(max_root_to_leaf_path(a))