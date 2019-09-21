#Question 1
def harmonic(n):
    s = 0
    for i in range(1,n+1):
        s += 1/i
    return s

def harmonicV2(n):
    return sum(1/i for i in range(1,n+1))


