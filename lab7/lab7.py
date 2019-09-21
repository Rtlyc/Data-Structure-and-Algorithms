#Problem 1

from DoublyLL import DoublyLinkedList

class LinkedStack:
    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self,elem):
        self.data.add_last(elem)

    def pop(self):
        if self.is_empty():
            raise Exception("The Stack is empty")
        val = self.data.delete_last()
        return val

    def top(self):
        if self.is_empty():
            raise Exception("The Stack is empty")
        val = self.data.last_node().data
        return val

##s = LinkedStack()
##for i in range(10):
##    s.push(i)
##print(s.pop())


#Problem 2

class LeakyStack1:
    CAPACITY = 5
    def __init__(self):
        self.data = [None] * LeakyStack1.CAPACITY
        self.n = 0
        self.last = None

    def __len__(self):
        return self.n

    def is_empty(self):
        return len(self) == 0

    def push(self,elem):
        if self.is_empty():
            self.last = -1
        self.last = (self.last + 1)%len(self.data)
        self.data[self.last] = elem
        ######
        self.n += 1
        if self.n > len(self.data):
            self.n = len(self.data)

    def pop(self):
        if self.is_empty():
            raise Exception("The LeakyStack is Empty")
        val = self.data[self.last]
        self.data[self.last] = None
        self.last = (self.last - 1) % len(self.data)
        self.n -= 1
        if self.is_empty():
            self.last = None
            self.n = 1
        return val

    def top(self):
        if self.is_empty():
            raise Exception("THe LeakyStack is Empty")
        return self.data[self.last]


s = LeakyStack1()
s.push(17)
s.push(42)
s.push(6)
s.push(31)
s.push(28)
print(s.data)
s.push(2)
print(s.data)
print(s.pop())
print(len(s))
print(s.pop())
print(s.data)

class LinkedLeakyStack:
    CAPACITY = 5
    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self,elem):
        if len(self) >= LinkedLeakyStack.CAPACITY:
            self.data.delete_first()
        self.data.add_last(elem)

    def pop(self):
        if self.is_empty():
            raise Exception("The LeakyStack is empty")
        return self.data.delete_last()

    def top(self):
        if self.is_empty():
            raise Exception("The LeakyStack is empty")
        return self.data.last_node().data

s = LinkedLeakyStack()
s.push(17)
s.push(42)
s.push(6)
s.push(31)
s.push(28)
print(s.data)
s.push(2)
print(s.data)
print(s.top())



from ArrayQueue import ArrayQueue

class QStack:
    def __init__(self):
        self.data = ArrayQueue()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self,elem): #O(1)
        self.data.enqueue(elem)

    def pop(self):#O(n)
        if self.is_empty():
            raise Exception("The QStack is empty")
        helper = ArrayQueue()
        for i in range(len(self) -1):
            helper.enqueue(self.data.dequeue())
        val = self.data.dequeue()
        self.data = helper
        return val

    def top(self):#O(n)
        if self.is_empty():
            raise Exception("The QStack is empty")
        helper = ArrayQueue()
        for i in range(len(self)):
            val = self.data.dequeue()
            helper.enqueue(val)
        self.data = helper
        return val

s = QStack()
for i in range(10):
    s.push(i)
for i in range(9):
    print(s.pop(),end= " ")
    
print(s.top())














    
