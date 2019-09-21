#Problem 1
class ArrayDeque:
    INITIAL_CAPACITY = 8
    def __init__(self):
        self.data = [None] * ArrayDeque.INITIAL_CAPACITY
        self.front = None
        self.back = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def first(self):
        if self.is_empty():
            raise Exception("Out of Range")
        return self.data[self.front]

    def last(self):
        if self.is_empty():
            raise Exception("Out of Range")
        return self.data[self.back]

    def enqueue_first(self,elem):
        if self.size == len(self.data):
            self.resize(2*len(self.data))
        if self.is_empty():
            self.front, self.back = 0,0
        else:
            self.front = (self.front + len(self.data) - 1) % len(self.data)
        self.data[self.front] = elem
        self.size += 1

    def enqueue_last(self,elem):
        if self.size == len(self.data):
            self.resize(2*len(self.data))
        if self.is_empty():
            self.front, self.back = 0,0
        else:
            self.back = (self.back + 1) % len(self.data)
        self.data[self.back] = elem
        self.size += 1

    def dequeue_first(self):
        if self.is_empty():
            raise Exception("The ArrayDeque is empty")
        elem = self.data[self.front]
        self.data[self.front] = None
        if self.size == 1:
            self.front = self.back = None
        else:
            self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return elem

    def dequeue_last(self):
        if self.is_empty():
            raise Exception("The ArrayDeque is empty")
        elem = self.data[self.back]
        self.data[self.back] = None
        if self.size == 1:
            self.front = self.back = None
        else:
            self.back = (self.back - 1 + len(self.data)) % len(self.data)
        self.size -= 1
        return elem

    def resize(self,capacity):
        new = [None] * capacity
        for i in range(self.size):
            index = (self.front + i) % len(self.data)
            new[i] = self.data[index]
        self.data = new
        self.front = 0
        self.back = (self.size - 1) % capacity

##d = ArrayDeque()
##for i in range(10):
##    d.enqueue_first(i)
##for i in range(10):
##    print(d.dequeue_first())

#Problem 2
from Stack import ArrayStack
d = {"}":"{","]":"[",")":"("}
def balanced_expression(str_input):
    stack = ArrayStack()
    for i in str_input:
        if i not in d:
            stack.push(i)
        else:
            try:
                output = stack.pop()
            except:
                return False
            if output != d[i]:
                return False   
    return stack.is_empty()
print(balanced_expression("([]{{[]}()})))))"))

#Problem 3
def get_tags(html_str):
    start_ind = html_str.find("<")
    end_ind = html_str.find(">",start_ind+1)
    while end_ind >= 0 and start_ind >= 0:
        yield html_str[start_ind+1:end_ind]
        start_ind = html_str.find("<",end_ind+1)
        end_ind = html_str.find(">",start_ind+1)

  
def is_mathced_html(html_str):
    stack = ArrayStack()
    for i in get_tags(html_str):
        if i[0] != "/":
            stack.push(i)
        else:
            try:
                val = stack.pop()
            except:
                return False
            if i[1:] != val:
                return False

    return stack.is_empty()
        













        
    

    
            
