import random
def binary_search(lst,val,low,high):
##    if low == high:
##        if lst[low] == val:
##            return low
##        return
    mid = (low + high) // 2
    if lst[mid] == val:
        return mid
    if low == high:
        return
    elif val > lst[mid]:
        return binary_search(lst,val,mid+1,high)
    else:
        return binary_search(lst,val,low,mid)

lst = [1,4,5,6,8,9,10,20,34,231,153214,13413411]
for i in lst:
    if binary_search(lst,i,0,len(lst)-1) == lst.index(i):
        pass
    else:
        print(i)


    
def nested_list_sum(lst,low,high):
    if low == high:
        if isinstance(lst[low],int):
            return lst[low]
        return nested_list_sum(lst[low],0,len(lst[low])-1)
    rest = nested_list_sum(lst,low+1,high)
    if isinstance(lst[low],int):
        return rest + lst[low]
    else:
        return rest + nested_list_sum(lst[low],0,len(lst[low])-1)

lst = [random.randint(0,3000) for i in range(50)]
s = nested_list_sum(lst,0,len(lst)-1)
if s != sum(lst):
    print(s)

def find_min(lst,low,high):
    if low == high:
        return low
    m = find_min(lst,low+1,high)
    if lst[low] > lst[m]:
        return m
    return low
#print(min(lst) == lst[find_min(lst,0,len(lst)-1)])
    
def selection_sort(lst):
    for i in range(len(lst)):
        k = find_min(lst,i,len(lst)-1)
        lst[i],lst[k] = lst[k],lst[i]
#selection_sort(lst)

def selection_sort_recursive(lst,low,high):
    if low == high:
        return
    k = find_min(lst,low,high)
    lst[low],lst[k] = lst[k],lst[low]
    selection_sort_recursive(lst,low+1,high)
selection_sort_recursive(lst,0,len(lst)-1)
#print(lst)

def partition(lst,low,high):
    pivot = lst[low]
    left = low
    right = high
    while left < right:
        if lst[left] > lst[right]:#左边大
            lst[left],lst[right] = lst[right],lst[left]
        if lst[left] == pivot:
            right -= 1
        else:
            left += 1
    return left


lst = [7,2,4,3,9,20,10,1,22,17]
print(partition(lst,0,len(lst)-1))

def quicksort(lst,start,end):
    mid = partition(lst,start,end)
    if start == end or mid == end:
        return
    quicksort(lst,start,mid)
    quicksort(lst,mid+1,end)
    
quicksort(lst,0,len(lst)-1)
print(lst)
    

                
        
    

    











    
    
