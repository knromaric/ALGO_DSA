class Node: 
    def __init__(self, value): 
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value + " -> "


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
a.next = b
b.next = c
c.next = d
d.next = e

# A -> B -> C -> D -> E

def print_linked_list(head): 
    current = head
    while current:
        print(current, end='')
        current = current.next 

def print_list_recursive(head): 
    if head is None: 
        return
    print(head, end='')
    print_list_recursive(head.next)


