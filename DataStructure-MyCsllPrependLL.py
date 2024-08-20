class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class CSLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp = self.head
        result = ''
        while temp:
            result+=str(temp.value)
            temp = temp.next
            if temp == self.head:
                break
            result+='->'
        return result

    def append(self,value):
        new_node = Node(value)
        if self.length==0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length+=1

    def prepend(self,value):
        new_node = Node(value)
        if self.length==0:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node
        self.length+=1




C = CSLL()
print('Before Prepending')
C.append(10)
C.append(20)
C.append(30)
print(C)
print('After Prepending')
C.prepend(5)
C.prepend(0)
print(C)

# Time Complexity = O(1)
# Space Complexity = O(1)