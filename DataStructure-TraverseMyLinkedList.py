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
            result +=str(temp_node.value)
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

    def insert(self,value,index):
        new_node = Node(value)
        if index<0 or index>self.length:
            return False
        elif self.length ==0:
            self.head = new_node
            self.tail = new_node
        elif index==0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length+=1
        return True

    def traverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next



n_l_l = LinkedList()
n_l_l.append(10)
n_l_l.prepend(20)
n_l_l.append(40)
print(n_l_l)
n_l_l.insert(60,1)
print(n_l_l)
n_l_l.traverse()


# Overall Time complexity is O(n)
# Overall Space complexity is O(1)