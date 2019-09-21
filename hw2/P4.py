#Question 4
from ArrayStack import ArrayStack

class MaxStack:
    def __init__(self):
        self.stack = ArrayStack()
        self._max = None

    def __len__(self):
        return len(self.stack)

    def is_empty(self):
        return len(self) == 0

    def push(self,elem):
        if self.is_empty():
            self._max = elem
        elif elem > self._max:
            self._max = elem
        self.stack.push((elem,self._max))

    def top(self):
        if self.is_empty():
            raise Exception("The max_s is empty")
        return self.stack.top()[0]

    def pop(self):
        if self.is_empty():
            raise Exception("The max_s is empty")
        elem = self.stack.pop()[0]
        if not self.is_empty():
            self._max = self.stack.top()[1]
        else:
            self._max = None
        return elem

    def max(self):
        if self.is_empty():
            raise Exception("The max_s is empty")        
        return self._max

