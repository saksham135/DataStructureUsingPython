
class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)

    # isEmpty
    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False

    def push(self,value):
        self.list.append(value)

    def pop(self):
        self.list.pop()

    def peek(self):
        return self.list[len(self.list)-1]

    def delete_all(self):
        self.list=None






my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
# my_stack.delete_all()
print(my_stack)