#Question 5
from ArrayStack import ArrayStack

class Queue:
    def __init__(self):
        self.stack = ArrayStack()
        self.helper = ArrayStack()

    def __len__(self):
        return len(self.stack)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self,elem):
        self.stack.push(elem)

    def first(self):
        if self.is_empty():
            raise Exception("The Queue is empty")
        for i in range(len(self)):
            self.helper.push(self.stack.pop())
        val = self.helper.top()
        for i in range(len(self)):
            self.stack.push(self.helper.pop())
        return val

    def dequeue(self):
        if self.is_empty():
            raise Exception("The Queue is empty")
        for i in range(len(self)):
            self.helper.push(self.stack.pop())
        val = self.helper.pop()
        for i in range(len(self.helper)):
            self.stack.push(self.helper.pop())
        return val
    
##q = Queue()
##for i in range(10):
##    q.enqueue(i)
##for i in range(10):
##    print(q.dequeue())

