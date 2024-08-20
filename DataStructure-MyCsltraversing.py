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
            result += str(temp.value)
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

    def prepend(self,value):
        new_node = Node(value)
        if self.length==0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node
        self.length+=1

    def insert(self,index,value):
        new_node = Node(value)
        if index<0 or index>self.length:
            return None
        elif index==0:
            if self.length==0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.tail.next = new_node
                self.head = new_node
        elif index==self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length+=1

    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
            if current==self.head:
                break






c=CSLL()
c.append(10)
c.append(20)
c.append(30)
c.prepend(5)
c.insert(2,15)
c.traverse()
