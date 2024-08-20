class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class CSLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length=0

    def append(self,value):
        new_node = Node(value)
        if self.length==0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length+=1


clss= CSLL()
clss.append(10)
clss.append(20)
print(clss.head.value)
print(clss.tail.value)


# Time Complexity for Both creation and appending the new element in the circular single Linked List is O(1)
# Space Complexity for Both Operation is also O(1) for both operations