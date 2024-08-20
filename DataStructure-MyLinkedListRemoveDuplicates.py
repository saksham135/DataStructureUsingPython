class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length=0

    def __str__(self):
        temp = self.head
        result = ''
        while temp is not None:
            result+=str(temp.value)
            if temp is not None:
                result+='->'
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
        self.length+=1

    # def remove_duplicates(self):
    #     if self.head is None:
    #         return None
    #     node_values = set()
    #     current = self.head
    #     node_values.add(current.value)
    #     while current.next:
    #         if current.next.value in node_values:
    #             current.next = current.next.next
    #             self.length-=1
    #         else:
    #             node_values.add(current.value)
    #             current = current.next
    #         self.tail = current

    def remove_duplicate(self):
        if self.head is None:
            return None
        node_values = set()
        current = self.head
        node_values.add(current.value)
        while current.next is not None:
            if current.next.value in node_values:
                current.next = current.next.next
                self.length-=1
            else:
                node_values.add(current.value)
                current=current.next
            self.tail = current



n_l_l = LinkedList()
n_l_l.append(10)
n_l_l.append(20)
n_l_l.append(30)
n_l_l.append(40)
n_l_l.append(50)
n_l_l.append(10)
print(n_l_l)
n_l_l.remove_duplicate()
print(n_l_l)