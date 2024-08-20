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
        curr = self.head
        result = ''
        while curr is not None:
            result +=str(curr.value)
            if curr is not None:
                result+='->'
            curr = curr.next
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
        dummyNode = Node(-1)
        dummyNode.next = self.head
        prev_node,curr_node = dummyNode,self.head
        while curr_node:
            if curr_node.value == value:
                prev_node.next = curr_node.next
            else:
                prev_node = curr_node
            curr_node = curr_node.next
        return dummyNode.next





n_l_l = LinkedList()
n_l_l.append(10)
n_l_l.append(20)
n_l_l.append(30)
n_l_l.append(20)
n_l_l.remove_elem(20)
print(n_l_l)