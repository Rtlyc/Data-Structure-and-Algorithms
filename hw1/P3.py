#Question 3
def leonardo(n):
    for i in range(n):
        if i == 1 or i == 0:
            a,b = 1,1
            yield 1
        else:
            a,b = b,a+b+1
            yield b


