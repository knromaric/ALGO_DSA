''' Linked List Value
    Write a function, linked_list_values, that takes in the head of a linked list as an argument.
    The function should return a list containing all values of the nodes in the linked list
'''


class Node: 
    def __init__(self, value): 
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value + " -> "

def linked_list_values(head): 
    values = []
    current = head
    while current: 
        values.append(current.value)
        current = current.next
    return values


# Solving the same problem using a recursive approach
def linked_list_values_recursive(head): 
    values = []
    fill_values(head, values)
    return values

def fill_values(head, values): 
    if not head: 
        return 
    values.append(head.value)
    fill_values(head.next, values)


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

print(linked_list_values(a))

print(linked_list_values_recursive(a))



## Complexity

'''
    Time Complexity: O(n)
    Space complexity: O(n)
'''