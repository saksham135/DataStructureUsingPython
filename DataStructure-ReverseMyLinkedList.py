class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def reverse(self):
        prev_node = None 
        current = self.head 
        while current is not None:
            next_node = current.next 
            current.next = prev_node 
            prev_node = current 
            current = next_node 
        self.tail,self.head = self.head,self.tail
        
        
n_l_l = LinkedList()
n_l_l.append(10)
n_l_l.append(20)
n_l_l.append(30)
n_l_l.append(40)
print(n_l_l)
print(n_l_l.reverse())