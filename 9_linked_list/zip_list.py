
'''Zip List
    Write a function, zipper_lists, that takes in the head of two linked lists as arguments. The function should zipper the two lists together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked list. 

    Do this in-place, by mutating the original Nodes

    You may assume that both input lists are non-empty
'''

from node import Node

def zip_list(head_1, head_2): 
    tail = head_1
    current_1 = head_1.next
    current_2 = head_2
    count = 0 

    while current_1 and current_2: 
        if count % 2 == 0: 
            tail.next = current_2
            current_2 = current_2.next
        else: 
            tail.next = current_1
            current_1 = current_1.next
        tail = tail.next
        count += 1
    
    if current_1 : 
        tail.next = current_1
    if current_2 : 
        tail.next = current_2

    return head_1


def zip_list_recursive(head_1, head_2): 
    if head_1 is None and head_2 is None: 
        return None
    if head_1 is None: 
        return head_2
    if head_2 is None: 
        return head_1

    next_1 = head_1.next
    next_2 = head_2.next
    head_1.next = head_2
    head_2.next = zip_list_recursive(next_1, next_2)
    return head_1 

def display_list(head): 
    current = head
    while current: 
        print(current, end='')
        current = current.next


## Tests 
a = Node('A')
b = Node('B')
c = Node('C')
a.next = b
b.next = c

x = Node('X')
y = Node('Y')
z = Node('Z')
x.next = y
y.next = z


# display_list(zip_list(a, x))
display_list(zip_list_recursive(a, x))