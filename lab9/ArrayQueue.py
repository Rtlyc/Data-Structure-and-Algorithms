class ArrayQueue:
    INITIAL_CAPACITY = 8
    def __init__(self):
        self.lst = [None] * ArrayQueue.INITIAL_CAPACITY
        self.size = 0
        self.front = None

    def __repr__(self):
        return str(list(self.lst))

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def enqueue(self,item):
        if self.size == len(self.lst):
            self.resize(2 * len(self.lst))
        if self.is_empty():
            self.front = 0
        back = (self.front + self.size) % len(self.lst)
        self.lst[back] = item
        self.size += 1
        

    def dequeue(self):
        if self.is_empty():
            return Exception("Empty Queue")
        elem = self.lst[self.front]
        self.lst[self.front] = None
        self.front = (self.front+1) % len(self.lst)
        self.size -= 1
        if self.is_empty():
            self.front = None
        if len(self) <= len(self.lst) // 4:
            self.resize(len(self.lst) // 2)
        return elem

    def first(self):
        if self.is_empty():
            return Exception("Empty Queue")
        return self.lst[self.front]

    def resize(self,capacity):
        new = [None] * capacity  
        for i in range(self.size):
            loc = (i + self.front) % len(self.lst)
            new[i] = self.lst[loc]
        self.front = 0
        self.lst = new
##q = ArrayQueue()
##for i in range(8):
##    q.enqueue(i)
##for i in range(8):
##    print(q.dequeue())
            
