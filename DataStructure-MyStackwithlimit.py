class Stack:
    def __init__(self,max_size):
        self.max_size = max_size
        self.list = []

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list)>self.max_size:
            return True
        else:
            return False

    def push(self,value):
        self.list.append(value)

    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[len(self.list)-1]


cs = Stack(5)
cs.push(10)
cs.push(15)
cs.push(20)
cs.push(30)
cs.push(40)
print(cs)
print(cs.peek())


