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
        current = self.head
        result = ''
        while current is not None:
            result+=str(current.value)
            if current is not None:
                result+='->'
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

# Method-1
#     def remove_duplicate(self):
#         current = self.head
#         while current is not None and current.next is not None:
#             if current.value == current.next.value:
#                 current.next = current.next.next
#             else:
#                 current = current.next
#         return current

# Method2:
    def remove_duplicate(self):
        if self.head is None:
            return None
        node_value = set()
        current = self.head
        node_value.add(current.value)
        while current.next:
            if current.next.value in node_value:
                current.next = current.next.next
                self.length-=1
            else:
                node_value.add(current.value)
                current = current.next
                self.length+=1
            return current





l1 = LinkedList()
l1.append(1)
l1.append(1)
l1.append(2)
l1.append(3)
l1.remove_duplicate()
print(l1)
