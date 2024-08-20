class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        current = self.head
        result =''
        while current:
            result+=str(current.value)
            if self.head is not None:
                result+='<->'
            current=current.next
        return result

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length+=1

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length+=1

    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current=current.next

    def reverse_traverse(self):
        current = self.tail
        while current:
            print(current.value)
            current=current.prev
        self.length+=1

    def search(self,value):
        current = self.head
        while current:
            if current.value==value:
                return True
            current=current.next
        return False

    def get(self,index):
        if index<0 or index>self.length:
            return None
        elif index<self.length//2:
            current = self.head
            for _ in range(index):
                current=current.next
        else:
            current = self.tail
            for _ in range(self.length-1,index,-1):
                current=current.prev
        return current

    def pop(self):
        if self.length==1:
            self.head = None
            self.tail = None
        elif self.length==0:
            return None
        else:
            popped_node = self.head
            self.head=self.head.next
            self.head.prev = None
            popped_node.next = None
            self.length-=1
            return popped_node

    def pop_tail(self):
        if self.length==1:
            self.head = None
            self.tail = None
        elif self.length==0:
            return None
        else:
            popped_node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.next = None
            self.length-=1
            return popped_node

    def remove(self,index):
        if index<0 or index>self.length:
            return None
        elif index==0:
            return self.pop()
        elif index==self.length-1:
            return self.pop_tail()
        else:
            popped_node = self.get(index)
            popped_node.prev.next = popped_node.next
            popped_node.next.prev = popped_node.prev
            popped_node.next = None
            popped_node.prev = None
            self.length-=1
            return popped_node





c=LinkedList()
c.append(10)
c.append(20)
c.append(30)
c.prepend(5)
print(c)

