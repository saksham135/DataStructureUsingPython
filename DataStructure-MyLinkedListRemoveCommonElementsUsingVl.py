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
        result =''
        while temp is not None:
            result+=str(temp.value)
            if temp is not None:
                result+='->'
            temp=temp.next
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

    def remove_elem(self,value):
        dummy_node = Node(-1)
        dummy_node.next = self.head

        prev_node,curr_node = dummy_node,self.head
        while curr_node:
            if curr_node.value==value:
                prev_node.next = curr_node.next
            else:
                prev_node = curr_node
            curr_node = curr_node.next
        return dummy_node.next




n_l_l = LinkedList()
n_l_l.append(1)
n_l_l.append(2)
n_l_l.append(6)
n_l_l.append(4)
n_l_l.append(5)
n_l_l.append(6)
n_l_l.remove_elem(2)
print(n_l_l)