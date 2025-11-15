'''
    
'''
from node import Node

def linked_list_find(head, target): 
    current = head
    while current: 
        if current.value == target: 
            return True
        current = current.next
    return False

def linked_list_find_recursive(head, target): 
    if not head: 
        return False
    if head.value == target:
        return True
    return linked_list_find_recursive(head.next, target)
        

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

print (linked_list_find(a, 'C'))
print (linked_list_find(a, 'G'))

print (linked_list_find_recursive(a, 'G'))
print (linked_list_find_recursive(a, 'B'))


# Complexity
"""
    linked_list_find
        Time complexity: O(n)
        Space complexity: O(1)

    linked_list_find_recursive
        Time Complexity: O(n)
        Space complexity: O(n)
"""