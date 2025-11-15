'''
    Write functions get_node and get_node_recursive, that take in the head of a linked list and an index. The function should return the value of the linked list at the specified index.
'''

from node import Node


def get_node(head, target_idx): 
    current = head
    count = 0
    while current: 
        if count == target_idx: 
            return current.value
        current = current.next
        count += 1
    return None

def get_node_recursive(head, target_idx): 
    if not head: 
        return None
    if target_idx == 0: 
        return head.value
    return get_node_recursive(head.next, target_idx-1)

# Tests 
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
a.next = b
b.next = c
c.next = d
d.next = e

print(get_node(a, 2))
print(get_node(a, 4))
print(get_node(a, 7))

print(get_node_recursive(a, 2))
print(get_node_recursive(a, 4))
print(get_node_recursive(a, 7))



# Complexity
"""
    get_node:
        Time complexity: O(n)
        Space complexity: O(1)

    get_node_recursive:
        Time Complexity: O(n)
        Space complexity: O(n)
"""