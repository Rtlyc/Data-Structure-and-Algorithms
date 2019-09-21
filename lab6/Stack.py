import ctypes

def make_array(num):
    return (ctypes.py_object * num)()

class ArrayStack:
    INITIAL_CAPACITY = 10
    def __init__(self):
        self.n = 0
        self.capacity = ArrayStack.INITIAL_CAPACITY
        self.lst = make_array(self.capacity)

    def __len__(self):
        return self.n

    def is_empty(self):
        return self.n == 0

    def push(self,item):
        if self.n == self.capacity:
            self.resize(self.capacity*2)
        self.lst[self.n] = item
        self.n += 1
            

    def pop(self):
        if self.is_empty():
            raise IndexError("Invalid")
        val = self.lst[self.n-1]
        self.lst[self.n-1] = None
        self.n -= 1
        return val

    def top(self):
        if self.is_empty():
            raise IndexError("Invalid")
        val = self.lst[self.n-1]
        return val

    def resize(self,capacity):
        new = make_array(capacity)
        for i in range(self.n):
            new[i] = self.lst[i]
        self.capacity = capacity
        self.lst = new

##stack = ArrayStack()
##for i in range(15):
##    stack.push(i)
##for i in range(5):
##    print(stack.pop())
