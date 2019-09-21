#Question 4
import ctypes
def make_array(n):
    return (ctypes.py_object * n)()

class MyList:
    def __init__(self):
        self.data = make_array(1)
        self.n = 0
        self.capacity = 1

    def __len__(self):
        return self.n

    def resize(self,new_capacity):
        new = make_array(new_capacity)
        for i in range(self.n):
            new[i] = self.data[i]
        self.capacity = new_capacity
        self.data = new

    def __getitem__(self,item):
        if not 0 <= item <= self.n:
            raise IndexError("Out of Range")
        return self.data[item]

    def __setitem__(self,item,value):
        if not 0 <= item <= self.capacity:
            raise IndexError("Out of Range")
        self.data[item] = value

    def append(self,val):
        if self.n == self.capacity:
            self.resize(self.capacity * 2)
        self.data[self.n] = val
        self.n += 1

    def extend(self,ls):
        # If self has m elements, and other has n elements
        # Running time: O(m + n)
        for i in ls:
            self.append(i)

    def pop(self,loc = -1):
        if loc < 0:
            loc += self.n
        if loc > self.n or loc < 0:
            raise ValueError("Invalid Value")
        val = self.data[loc]
        for i in range(loc,self.n-1):
            self.data[i] = self.data[i+1]
        self.n -= 1
        return val

    def insert(self,loc,val):
        if self.n == self.capacity:
            self.resize(self.capacity * 2)
        for i in range(self.n,loc,-1):
            self[i] = self[i-1]
        self.data[loc] = val
        self.n += 1
            

    def remove(self,val):
        for i in range(self.n):
            if self.data[i] == val:
                self.pop(i)
                break
        else:
            raise ValueError("Can't find")

    def __iter__(self):
        for i in range(self.n):
            yield self.data[i]

    def __repr__(self):
        if len(self) == 0:
            return "[]"
        s = "["
        for i in self.data[:len(self)-1]:
            s += str(i) + ", "
        s += str(self.data[len(self)-1]) + "]"
        return s

    def __add__(self,other):
        n = MyList()
        n.extend(self)
        n.extend(other)
        return n

    def __mul__(self,other):
        n = MyList()
        for i in range(other):
            n += self
        return n

    def __rmul__(self,other):
        return self * other

    def __iadd__(self,other):
        self.extend(other)
        return self


m = MyList()
m.extend([2,3])
n = MyList()
n.extend(m.data)
n.append(10)
print(m+n)

