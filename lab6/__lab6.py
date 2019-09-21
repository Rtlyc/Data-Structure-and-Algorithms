#Problem 1

class ArrayDeque:
    CAPACITY = 8
    def __init__(self):
        self.data = [None] * ArrayDeque.CAPACITY
        self.size = 0
        self.front = None
        self.back = None

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def first(self):
        if self.is_empty():
            raise Exception("The Deque is Empty")
        return self.data[self.front]

    def last(self):
        if self.is_empty():
            raise Exception("The Deque is Empty")
        return self.data[self.back]

    def enqueue_first(self,elem):
        if self.size == len(self.data):
            self.resize(2 * len(self.data))
        if self.is_empty():
            self.front = self.back = 0
        else:
            self.front = (self.front - 1)%len(self.data)
        self.data[self.front] = elem
        self.size += 1

    def enqueue_last(self,elem):
        if self.size == len(self.data):
            self.resize(2 * len(self.data))
        if self.is_empty():
            self.front = self.back = 0
        else:
            self.back = (self.back + 1) % len(self.data)
        self.data[self.back] = elem
        self.size += 1

    def dequeue_first(self):
        if self.is_empty():
            raise Exception("The Deque is Empty")
        val = self.data[self.front]
        self.data[self.front] = None
        if self.is_empty():
            self.front = self.back = None
        else:
            self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return val

    def dequeue_last(self):
        if self.is_empty():
            raise Exception("The Deque is Empty")
        val = self.data[self.back]
        self.data[self.back] = None
        if self.is_empty():
            self.front = self.back = None
        else:
            self.back = (self.back - 1) % len(self.data)
        self.size -= 1
        return val

    def resize(self,capacity):
        new = [None] * capacity
        for i in range(self.size):
            index = (self.front + i) % len(self.data)
            new[i] = self.data[index]
        self.data = new


#Problem 2
from Stack import ArrayStack

def balanced_expression(str_input):
    d = {"}":"{",")":"(","]":"["}
    stack = ArrayStack()
    for i in str_input:
        if i in "{[(":
            stack.push(i)
        else:
            try:
                out = stack.pop()
                if out != d[i]:
                    return False
            except:
                return False
    return stack.is_empty()
input_str = "([]{{[]})})"
#print(balanced_expression(input_str))

#Problem 3
def get_tokens(input_str):
    start_ind = input_str.find("<")
    end_ind = input_str.find(">",start_ind)
    while start_ind != -1 and end_ind != -1:
        yield input_str[start_ind:end_ind+1]
        start_ind = input_str.find("<",end_ind)
        end_ind = input_str.find(">",start_ind)
input_str = "af<abcd><asdf>asdflj</asdf>>asfsa</abcd>"
for i in get_tokens(input_str):
    print(i)

def is_matched_html(html_str):
    lst = [i for i in get_tokens(html_str)]
    stack = ArrayStack()
    for i in lst:
        if i[1] == "/":
            try:
                out = stack.pop()
                if out[1:-1] != i[2:-1]:
                    return False
            except:
                return False
        else:
            stack.push(i)
    return stack.is_empty()
print(is_matched_html(input_str))
                









        
