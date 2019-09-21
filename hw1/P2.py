#Question 2
import math
def find_primes(n):
    lst = []
    for j in range(1,n+1):
        count = 0
        for i in range(2,int(math.sqrt(j))+1):
            if j % i == 0:
                count += 1
        if count < 1 and j != 1:
            lst.append(j)
    return lst

def prime_seive(n):
    lst = [True] * (n+1)
    for num in range(2,n+1):
        for item in range(1,n+1):
            if item % num == 0 and item != num:
                lst[item] = False
    return [k for k in range(2,n+1) if lst[k]]

