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
            if temp==self.head:
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

cs=CSLL()
cs.append(10)
cs.append(20)
cs.append(30)
print(cs)

# Time complexity = O(n)