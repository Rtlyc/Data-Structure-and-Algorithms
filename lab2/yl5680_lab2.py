#5x^3 − 17x^1 + 42x^0
#[42,-17,0,5]
class Polynomial:
    def __init__(self,lst):
        self.lst = lst

    def __repr__(self):
        lst = [str(self.lst[n])+"x^"+str(n) for n in range(len(self.lst)-1,-1,-1)]
        return "+".join(lst)

    def eval(self,value):
        s = 0
        for i in range(len(self.lst)):
            s += (value **i) * self.lst[i]
        return s

    def __add__(self,other):
        ls = []
        count = 0
        try:
            while True:
                ls.append(self.lst[count]+other.lst[count])
                count += 1
        except:
            ls.extend(self.lst[count:])
            ls.extend(other.lst[count:])
        return Polynomial(ls)

    def __mul__(self,other):
        ls = [0]
        p = Polynomial(ls)
        for i in range(len(self.lst)):
            lst = [0] * i
            for j in other.lst:
                lst.append(self.lst[i]*j)
            p = p + Polynomial(lst)
        return p           

    def polySequence(self,start,end,step = 1):
        for i in range(start,end,step):
            yield self.eval(i)

    def derive(self):
        if len(self.lst) <= 1:
            return 0
        ls = [self.lst[i]*i for i in range(1,len(self.lst))]
        return Polynomial(ls)

def main():
    p = Polynomial([42,-17,0,5])
    p1 = Polynomial([1,1])
    p2 = Polynomial([3,2])
    pp = Polynomial([1,2])
    p4 = Polynomial([1,4,0,2])
    print(p4+p)
    for val in pp.polySequence(0,5):
        print(val)

