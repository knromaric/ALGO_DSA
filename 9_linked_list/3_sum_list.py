'''Sum List
    Write a function, sum_list, that takes in the head of a linked list containing numbers as an
    argument. The function should return the total sum of all values in the linked list.
'''

from node import Node


def sum_list(head): 
    current = head
    sum = 0
    while current: 
        sum += current.value
        current = current.next 
    return sum


def sum_list_recursive(head): 
    if not head: 
        return 0
    return head.value + sum_list_recursive(head.next)

## Tests 
a = Node(5)
b = Node(7)
c = Node(4)
d = Node(2)
e = Node(1)
a.next = b
b.next = c
c.next = d
d.next = e

print(sum_list(a))
print(sum_list_recursive(a))