class Stack:
    def __init__(self):
        self.list = []   # Time and Space for creating an empty with no size limit is O(1)

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)

    # stack methods
    #1.isEmpty
    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False

    def push(self,value):
        self.list.append(value)
        return "The Element has been succesfully implemented in the stack"
    # time complexity for insertion in stack is O(n) since it is amortized insertion and in worest case it is O(n2) and space complexity is O(1)

    def pop(self):
        if self.isEmpty():
            return "There are no elements pressnt inside the stack"
        else:
            return self.list.pop()     #.pop() is inbuilt stack pop method used in python
        # time complexity and space complexity for both push and pop is O(1)

    def pick(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            return self.list[len(self.list)-1]



my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.pop()
print(my_stack)
