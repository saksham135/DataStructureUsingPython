class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

class Queue:
    def __iter__(self):
        self.ll = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.ll]
        return '->'.join(values)

    def enqueue(self,value):
        new_node = Node(value)
        if self.ll.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.ll.tail.next = new_node
            self.tail = new_node

    def isempty(self):
        if self.ll.head is None:
            return True
        else:
            return False

    def deque(self):
        if self.isempty():
            return 'No Elements in the Queue'
        else:
            temp = self.ll.head
            if self.ll.head == self.ll.tail:
                self.ll.head = None
                self.ll.tail = None
            else:
                self.ll.head = self.ll.head.next
            return temp

    def peek(self):
        if self.isempty():
            return 'No Element in the Queue'
        else:
            return self.ll.head




c = Queue()
c.enqueue(1)
c.enqueue(2)
c.enqueue(3)
print(c.peek())