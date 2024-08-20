# Question - Describe how could you use a single python list to implement 3 stacks in a single stack.


class Multistack:
    def __init__(self,stacksize):
        self.noofstack = 3
        self.custlist = [0]*(stacksize*self.noofstack)
        self.size = [0]*self.noofstack
        self.stacksize = stacksize

    def isFull(self,stacknum):
        if self.size[stacknum]==self.stacksize:
            return True
        else:
            return False


    def isempty(self,stacknum):
        if self.size[stacknum]==0:
            return True
        else:
            return False

    def inde_top(self,stacknum):
        offset = stacknum * self.stacksize
        return offset+self.size[stacknum-1]

    
