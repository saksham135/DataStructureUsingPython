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

class Merge:
    def merge(self,l1,l2):
        prehead = Node(-1)
        prev = prehead
        while l1 and l2:
            if l1.val <=l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if l1 is not None else l2
        return prev.next


n_l_l = LinkedList()
n_l_l.append(1)
n_l_l.append(2)
n_l_l.append(3)
n_l_l_1 = LinkedList()
n_l_l_1.append(1)
n_l_l_1.append(3)
n_l_l_1.append(4)
print(n_l_l)
print(n_l_l_1)
m_l_l = Merge()
print(m_l_l.merge(n_l_l,n_l_l_1))



