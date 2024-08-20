class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1


n_l_l = LinkedList()
n_l_l.append(10)
n_l_l.append(20)
print(n_l_l.head.value)
print(n_l_l.length)
print(n_l_l.tail.value)
print(n_l_l)


# Time Complexity = O(1)
# Space Complexity - O(1)