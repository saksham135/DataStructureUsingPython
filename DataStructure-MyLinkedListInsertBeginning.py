class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result =''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node is not None:
                result += '->'
            temp_node = temp_node.next
        return result

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1


n_l_l = LinkedList()
n_l_l.append(10)
n_l_l.append(20)
n_l_l.append(30)
print(n_l_l)
n_l_l.prepend(40)
print(n_l_l)


# Overall Time Complexity is O(1)
# Overall Space complexity is O(1)