#Problem 1
def binary_search(lst,val,low,high):
    mid = (low+high)//2
    if lst[mid] == val:
        return mid
    if low == high:
        return -1
    else:
        if lst[mid] < val:
            return binary_search(lst,val,mid+1,high)
        else:
            return binary_search(lst,val,low,mid)

lst = [2,7,8,9,10]
#print(binary_search(lst,9,0,len(lst)-1))

#Problem 2
def nested_list_sum(lst,low,high):
    if low == high:
        if isinstance(lst[low],int):
            return lst[low]
        return nested_list_sum(lst[low],0,len(lst[low])-1)
    if isinstance(lst[low],int):
        return lst[low] + nested_list_sum(lst,low+1,high)
    return nested_list_sum(lst[low],0,len(lst[low])-1) + nested_list_sum(lst,low+1,high)
nested_lst =  [1, [2, 3], 4, [5, [6, [7, 8]], 9], 10]
nested_lst =  [1, [2, [3], [4, 5]], [6, 7]]
#print(nested_list_sum(nested_lst,0,len(nested_lst)-1))

#Problem 3
def find_min(lst,low,high):
    if low == high:
        return low
    loc = find_min(lst,low+1,high)
    cur = lst[loc]
    if lst[low] < cur:
        return low
    return loc

def selection_sort(lst):
    left = 0
    right = 0
    while left < len(lst)-1:
        right = find_min(lst,left,len(lst)-1)
        lst[left],lst[right] = lst[right],lst[left]
        left += 1
        

#lst = [634,51,6,1,31,32,21,41,5,25,4]
#selection_sort(lst)
#print(lst)

def selection_sort_recursive(lst,low,high):
    if low == high:
        return
    loc = find_min(lst,low,high)       
    lst[low],lst[loc] = lst[loc],lst[low]
    selection_sort_recursive(lst,low+1,high)
#lst = [34,51,6,1,31,32,21,41,5,25,4]
#selection_sort_recursive(lst,0,len(lst)-1)
#print(lst)

#Problem 4
def partition(lst,low,high):
    left = low
    right = high
    pivot = lst[low]
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

def quicksort(lst,start,end):
    if start == end:
        return
    pivot = lst[start]
    partition(lst,start,end)
    for i in range(start,end):
        if lst[i] == pivot:
            first_end = i
            break
    quicksort(lst,start,first_end)
    quicksort(lst,first_end+1,end)

quicksort(lst,0,len(lst)-1)
#print(lst)
    
        
    

        
        











