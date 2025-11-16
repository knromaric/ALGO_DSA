
'''Reverse List
    Write a function, reverse_list, that takes in the head of a linked list as an argument. The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.
'''

from node import Node

def reverse_list(head): 
    previous = None
    current = head
    while current: 
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous


def reverse_list_recursive(head, previous=None): 
    if not head: 
        return previous
    next = head.next
    head.next = previous
    return reverse_list_recursive(next, head)



def display_list(head): 
    current = head
    while current: 
        print(current, end='')
        current = current.next
    




## Tests 
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
a.next = b
b.next = c
c.next = d
d.next = e

print("-- Linked List --")
display_list(a)

print()
print("-- Reverse linked list --")
# display_list(reverse_list(a))
print()
display_list(reverse_list_recursive(a))

