
from tree_node import Node
from collections import deque


def tree_includes(root, target): 
    if not root: 
        return False
    queue = deque([root])

    while queue: 
        current_node = queue.popleft()
        if current_node.val == target: 
            return True
        else: 
            if current_node.left: 
                queue.append(current_node.left)
            if current_node.right: 
                queue.append(current_node.right)
            
    return False


def tree_includes_recursive(root, target): 
    if not root: 
        return False
    if root.val == target: 
        return True
    
    return tree_includes_recursive(root.left, target) or tree_includes_recursive(root.right, target)

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

print(tree_includes(a, "e"))
print(tree_includes(a, "g"))

print(tree_includes_recursive(a, "e"))
print(tree_includes_recursive(a, "g"))