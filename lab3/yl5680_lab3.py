#Problem 1

def first1(lst):
    start = 0
    end = len(lst) -1
    if lst[start] == 1:
        return start
    while start <= end:
        mid = (start+end)//2
        if lst[mid] == 0:
            start = mid + 1
        elif lst[mid] == 1:
            if lst[mid-1] == 0:
                return mid
            else:
                end = mid
lst = [0,0,0,1]
#lst =[1]
print(first1(lst),"first1")

#Problem 2

def e_approximation(n):
    s = 1
    pre = 1
    for i in range(1,n+1):
        pre = pre * i
        s += 1/pre
    return s

print(e_approximation(17),"e_approxi")


#Problem 3
def two_sum(sorted_lst,target):
    left = 0
    right = len(sorted_lst)-1
    while left < right:
        cur = sorted_lst[left] + sorted_lst[right]
        if cur == target:
            return left,right
        elif cur < target:
            left += 1
        else:
            right -= 1
ls = [-3,-2,0,5,17]
print(two_sum(ls,3),"two_sum")

#Problem 4
def split_neg_pos(lst):
    left = 0
    right = len(lst)-1
    while left < right:
        if lst[left] > 0:
            if lst[right] < 0:
                lst[left],lst[right] = lst[right],lst[left]
                left += 1
                right -= 1
            else:
                right -= 1
        else:
            left += 1
lst = [-7,5,-3,4,2,-6,5,-2]
split_neg_pos(lst)
print(lst,"split_neg")

#Problem 5
def move_zeros(lst):
    left = 0
    right = 0
    while right < len(lst):
        if lst[left] == 0:
            if lst[right] != 0:
                lst[left],lst[right] = lst[right],lst[left]
            else:
                right += 1
        else:
            left += 1
            right = left
            
lst = [1,0,0,2,3,0,0,0,4,0,5,0]
move_zeros(lst)
print(lst,"move_zeros")

#Problem 6
def find_min(lst,start,end):
    if start == end:
        return lst[start]
    num = find_min(lst,start+1,end)
    if lst[start] < num:
        return lst[start]
    return num
lst = [5,-1,9,6,0]
print(find_min(lst,0,4),"find_min")
            
    
                
        













            
