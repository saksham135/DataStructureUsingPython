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
        current = self.head
        result = ''
        while current is not None:
            result += str(current.value)
            if current is not None:
                result +='->'
            current = current.next
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

    def remove_duplicate(self):
        my_set = set()
        current = self.head
        my_set.add(current.value)
        while current.next:
            if current.next.value in my_set:
                current.next=current.next.next
                self.length-=1
            else:
                my_set.add(current.value)
                current=current.next
            self.tail=current




n_l_l = LinkedList()
n_l_l.append(1)
n_l_l.append(1)
n_l_l.append(2)
n_l_l.append(3)
print(n_l_l)
n_l_l.remove_duplicate()
print(n_l_l)