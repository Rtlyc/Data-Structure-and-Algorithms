#Problem 1
#[50,55,65,70,75,80,85,95]

#Problem 3
# a. O(n)
# b. O(n^2)

#Problem 4
# 36
"""
sum_list1(lst,low,high): O(n)
sum_list2(lst,low,high): O(logn)
"""
#Problem 5
#a) O(n^2)
#b)
import random
def random_str(n):
    letters = "abcdefghijklmnopqrstuvwxyz"
    lst = []
    for i in range(1,n+1):
        curr = random.choice(letters)
        lst.append(curr)
    return " ".join(lst)
#print(random_str(10))

#Problem 6
def powers(base,n):
    for i in range(1,n+1):
        yield base ** i

##for val in powers(3, 5):
##    print(val, end=' ')

#Problem 7
def is_palindrome(input_str,low,high):
    if low == high-1:
        return True
    if input_str[low] == input_str[high-1] and is_palindrome(input_str,low+1,high-1):
        return True
    return False
input_str = "kldajf"
#print(is_palindrome(input_str,0,len(input_str)))


#Problem 8
def partition(lst):
    left = 0
    right = len(lst) -1
    pivot = lst[0]
    while left < right:
        if lst[left] < lst[right]:
            if lst[right] != pivot:
                right -= 1
            else:
                left += 1
        elif lst[left] > lst[right]:
            lst[left],lst[right] = lst[right],lst[left]
            if lst[left] != pivot:
                left += 1
            else:
                right -= 1
ls = [99, 17, 81, 77, 68, 22, 55, 10, 90,1,5]
partition(ls)
#print(ls)








        








