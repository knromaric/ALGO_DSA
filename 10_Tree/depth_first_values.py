'''
Write a function, depth_first_values, that takes in the root of a binary tree. The function
should return a list containing all values of the tree in depth-first order.

'''


from tree_node import Node

def depth_first_values(root): 
    if not root: 
        return []

    stack = [root]
    values = []
    while stack: 
        current_node = stack.pop()
        values.append(current_node.val)
    
        if current_node.right:  
            stack.append(current_node.right)
        if current_node.left: 
            stack.append(current_node.left)
    return values


def depth_first_values_recursive(root): 
    if not root: 
        return []
    left_values = depth_first_values_recursive(root.left)
    right_values = depth_first_values_recursive(root.right)
    return [root.val, *left_values, *right_values]


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

print(depth_first_values(a))
print(depth_first_values_recursive(a))


empty_node = None
print(depth_first_values(empty_node))
print(depth_first_values_recursive(empty_node))


# Complexity
"""
    depth_first_values:
        Time complexity: O(n)
        Space complexity: O(n)

    depth_first_values_recursive:
        Time Complexity: O(n)
        Space complexity: O(n)
""" 