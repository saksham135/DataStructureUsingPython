class Stack:
    def __init__(self,maxsize):
        self.items = maxsize*[None]
        self.maxsize = maxsize
        self.start = -1
        self.top = -1

    def __str__(self):
        value = [str(x) for x in self.items]
        return ' '.join(value)

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxsize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False

    def enque(self,value):
        if self.isFull():
            return 'The Queue is Full'
        elif self.top+1 == self.maxsize:
            self.top=0
        else:
            self.top+=1
            if self.start==-1:
                self.start=0
        self.items[self.top]=value

    def deque(self):
        if self.isEmpty():
            return 'There is no element in the queue'
        else:
            first_elem = self.items[self.start]
            start = self.start
            if self.start==self.top:
                self.start=-1
                self.top=-1
            elif


c=Stack(3)
c.enque(1)
c.enque(2)
c.enque(3)
print(c)
