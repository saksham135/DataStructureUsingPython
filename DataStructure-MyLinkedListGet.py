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
            result+=str(temp_node.value)
            if temp_node is not None:
                result+='->'
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

    def insert(self,index,value):
        new_node = Node(value)
        if index<0 or index>self.length:
            return False
        elif self.length==0:
            self.head = new_node
            self.tail = new_node
        elif index==0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length+=1
        return True

    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def search(self,target):
        temp = self.head
        while temp is not None:
            if temp.value==target:
                return True
            temp = temp.next
        return False

    # def get(self,index):
    #     current = self.head
    #     for _ in range(index):
    #         current = current.next
    #     return current.value

    # using index cases
    def get(self,index):
        if index==-1:
            return self.tail.value
        if index<-1 or index>self.length:
            return False
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value



n_l_l = LinkedList()
n_l_l.append(10)
n_l_l.append(20)
n_l_l.prepend(30)
n_l_l.insert(1,25)
print(n_l_l)
n_l_l.traverse()
print(n_l_l.search(25))
print(n_l_l.search(44))
print(n_l_l.get(2))


# Time complexity is O(n)
# Space Complextiy is O(1)