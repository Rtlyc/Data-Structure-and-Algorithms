#Question 2

def flatten_nested_list(lst, low, high):
    if isinstance(lst[low],int):
        left = [lst[low]]
    else:
        left = flatten_nested_list(lst[low],0,len(lst[low])-1)
    if low == high:
        return left
    right = flatten_nested_list(lst,low+1,high)
    return left + right

##nested_lst =  [1, [2, 3], 4, [5, [6, [7, [8]]],[9], 10]]
##lst = flatten_nested_list(nested_lst, 0, 3)
##print(lst)
                             
