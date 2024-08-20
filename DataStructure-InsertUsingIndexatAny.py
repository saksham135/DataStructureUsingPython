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
        temp = self.head
        result = ''
        while temp is not None:
            result += str(temp.value)
            if temp is not None:
                result+= '->'
            temp = temp.next
        return result

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1

    # # for inserting at any index
    # def insert(self,index,value):
    #     new_node = Node(value)
    #     temp_node = self.head
    #     for _ in range(index-1):
    #         temp_node = temp_node.next
    #     new_node.next = temp_node.next
    #     temp_node.next = new_node
    #     self.length+=1

    # for inserting at beginning as well
    # def insert(self,index,value):
    #     new_node = Node(value)
    #     if index==0:
    #         new_node.next = self.head
    #         self.head = new_node
    #     else:
    #         temp_node = self.head
    #         for _ in range(index-1):
    #             temp_node = temp_node.next
    #         new_node.next = temp_node.next
    #         temp_node.next = new_node
    #     self.length+=1

    # # if linked list is empty as well
    # def insert(self,index,value):
    #     new_node = Node(value)
    #     if self.length==0:
    #         self.head = new_node
    #         self.tail = new_node
    #     elif index==0:
    #         new_node.next = self.head
    #         self.head = new_node
    #     else:
    #         temp_node = self.head
    #         for _ in range(index-1):
    #             temp_node = temp_node.next
    #         new_node.next = temp_node.next
    #         temp_node.next = new_node
    #     self.length+=1


    # if index is less than 0 or greater than the length of linked list
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
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length+=1
        return True


n_l_l = LinkedList()
n_l_l.append(15)
n_l_l.append(20)
n_l_l.append(30)
print(n_l_l)
n_l_l.prepend(25)
print(n_l_l)
n_l_l.insert(-2,110)
print(n_l_l)



# Overall Time complexity is O(N)
# overall space complexity is O(1)