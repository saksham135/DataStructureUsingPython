class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)
class CDLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length=0

    def __str__(self):
        current = self.head
        result = ''
        while current:
            result+=str(current.value)
            current=current.next
            if current==self.head:
                break
            result+='<->'
        return result

    def append(self,value):
        new_node = Node(value)
        if self.length==0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail = new_node
        self.length+=1

    def prepend(self,value):
        new_node = Node(value)
        if self.length==0:
            self.head = new_node
            self.tail = new_node
            new_node.prev = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = self.tail
            self.head = new_node
        self.length+=1

    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current=current.next
            if current==self.head:
                break

    def reverse_traverse(self):
        current=self.tail
        while current:
            print(current.value)
            current=current.prev
            if current==self.tail:
                break

    def search_elem(self,target):
        current=self.head
        while current:
            if current.value==target:
                return True
            current=current.next
            if current==self.head:
                break
        return False

    def get_elem(self,index):
        current = None
        if index<self.length//2:
            current = self.head
            for i in range(index):
                current = current.next
        else:
            current = self.tail
            for i in range(self.length-1,index,-1):
                current = current.prev
        return current

    def set_elem(self,index,value):
        temp = self.get_elem(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert_elem(self,index,value):
        new_node = Node(value)
        if index<0 or index>self.length:
            return None
        elif index==0:
            return self.append(new_node)
        elif index==self.length:
            return self.prepend(new_node)
        else:
            current = self.get_elem(index-1)
            new_node.next = current.next
            current.next.prev = new_node
            current.next = new_node
            new_node.prev = current
            self.length+=1

    def pop(self):
        popped_node = self.head
        if self.length==1:
            self.head = None
            self.tail = None
        elif self.length==0:
            return None
        else:
            self.head = popped_node.next
            self.head.prev = self.tail
            self.tail.next = self.head
            popped_node.next = None
            popped_node.prev = None
            self.length-=1
        return popped_node

    def pop_last(self):
        popped_node = self.tail
        if self.length==1:
            self.head= None
            self.tail = None
        elif self.length==0:
            return None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
            popped_node.next = None
            popped_node.prev = None
            self.length-=1
        return popped_node

    def remove_elem(self,index):
        if index<0 or index>self.length:
            return None
        elif index==0:
            return self.pop()
        elif index==self.length-1:
            return self.pop_last()
        else:
            popped_node = self.get_elem(index)
            popped_node.prev.next = popped_node.next
            popped_node.next.prev = popped_node.prev
            popped_node.next = None
            popped_node.prev = None
            self.length-=1
        return popped_node

    def delete_all(self):
        self.head = None
        self.tail = None
        print('Noded Deleted')







ll=CDLL()
ll.append(10)
ll.append(20)
ll.append(30)
ll.prepend(5)
print(ll)
ll.delete_all()
print(ll)
