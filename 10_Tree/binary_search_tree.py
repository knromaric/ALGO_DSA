
class Node: 
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree: 
    def __init__(self):
        self.root = None

    def insert(self, new_value): 
        new_node = Node(new_value)
        if not self.root: 
            self.root = new_node
            return self
        current_node = self.root
        while new_value != current_node.value: 
            if new_value < current_node.value: 
                if not current_node.left: 
                    current_node.left = new_node
                    break
                current_node = current_node.left
            else: 
                if not current_node.right: 
                    current_node.right = new_node
                    break
                current_node = current_node.right
        return self

    def contains(self, value): 
        '''
        This function return True when it finds the "search_value" and false otherwise  
        '''
        current_node = self.root
        while current_node: 
            if value == current_node.value: 
                return True
            if value > current_node.value: 
                current_node = current_node.right
            else: 
                current_node = current_node.left
        return False
        
    def remove(self, value, start=None, parent=None): 
        current_node = start or self.root
        while current_node and current_node.value != value: 
            parent = current_node
            if value < current_node.value:
                current_node = parent.left
            else: 
                current_node = parent.right
        if not current_node: 
            raise Exception("Item not in tree")
        if not current_node.right and not current_node.left: 

            
        
