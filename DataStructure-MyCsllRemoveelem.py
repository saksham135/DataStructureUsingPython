class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
class CSLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        current = self.head
        result=''
        while current:
            result+=str(current.value)
            current = current.next
            if current==self.head:
                break
            result+='->'
        return result

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node
        self.length+=1

    def insert_elem(self,index,value):
        new_node = Node(value)
        if index<-1 or index>self.length:
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
                temp=temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length+=1

    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current=current.next
            if current==self.head:
                break

    def search_elem(self,value):
        current = self.head
        while current:
            if current.value==value:
                return True
            current=current.next
            if current==self.head:
                break
        return False

    def get_elem(self,index):
        if index<-1 or index>self.length:
            return None
        elif index==-1:
            return self.tail
        else:
            current=self.head
            for _ in range(index):
                current=current.next
            return current

    def post_elem(self,index,value):
        temp = self.get_elem(index)
        if temp:
            temp.value = value
            return True
        return False

    def pop_elem(self):
        popped_node = self.head
        if self.length==0:
            return None
        elif self.length==1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        self.length-=1
        return popped_node

    def pop(self):
        popped_node = self.head
        if self.length==0:
            return None
        elif self.length==1:
            self.head = None
            self.tail = None





c=CSLL()
c.append(10)
c.append(20)
c.append(30)
c.prepend(5)
c.insert_elem(2,15)
c.post_elem(2,13)
print(c)