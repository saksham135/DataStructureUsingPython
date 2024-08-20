
class Node:
    def __init__(self, value):
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
    def __init__(self):
        self.LL = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.LL]
        return '->'.join(values)

    def enqueue(self, value):
        new_node = Node(value)
        if self.LL.head is None:
            self.LL.head = new_node
            self.LL.tail = new_node
        else:
            self.LL.tail.next = new_node
            self.LL.tail = new_node

    def isempty(self):
        if self.LL.head is None:
            return True
        else:
            return False

    def deqeue(self):
        if self.isempty():
            return False
        else:
            temp = self.LL.head
            if self.LL.head == self.LL.tail:
                self.LL.head = None
                self.LL.tail = None
            else:
                self.LL.head = self.LL.head.next
            return temp

    def peek(self):
        if self.isempty():
            return 'No Element in the queue'
        else:
            return self.LL.head


c = Queue()
c.enqueue(1)
c.enqueue(2)
c.enqueue(3)
print(c.peek())