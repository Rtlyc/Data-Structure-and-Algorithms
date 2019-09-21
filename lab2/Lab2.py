class Polynomial:
    def __init__(self, lst = [0]):
        self.data = lst
    def __add__(self,other):
        lst = []
        lst2 = self.data.copy()
        lst3 = other.data.copy()
        if len(self.data)> len(other.data):
            for i in range (len(self.data) - len(other.data)):
                lst3.append(0)
        elif len(self.data) < len(other.data):
            for i in range (len(other.data) - len(self.data)):
                lst2.append(0)
        for i in range (len(lst2)):
            for j in range (len(lst3)):
                if i == j:
                    lst.append(lst2[i]+lst3[i])
        lst1 = Polynomial(lst)
        return lst1
    def __call__(self,n):
        ans = 0
        for i in range (len(self.data)):
            ans += self.data[i]*n**i
        return ans
    def __str__(self):
        s = "";
        for i in range (len(self.data)):
            s = " + " +str(self.data[i]) + "x^" + str(i) +  s
        return s
    def __mul__(self, other):
        lst = []
        for i in range (len(self.data) + len(other.data)):
            lst.append(0)
        for i in range (len(self.data)):
            for j in range (len(other.data)):
                other.data[j]
        
            
poly1 = Polynomial([3, 7, 0, -9, 2])
poly2 = Polynomial([2, 0, 0, 5, 0, 0, 3])
poly3 = poly1 + poly2
print(poly3.data)
print(poly1)
print(poly2(1))
