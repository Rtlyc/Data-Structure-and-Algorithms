#Question 3

def permutations(lst, low, high):
    if low == high:
        answer = [lst[low]]
        return [answer]
    first = lst[low]
    cur_lst = permutations(lst,low+1,high)
    answer = []
    for sublist in cur_lst:
        for index in range(high-low+1):
            copy = sublist.copy()
            copy.insert(index,first)
            answer.append(copy)
    return answer
##lst = [1,2,3,4]
##print(permutations(lst,0,3))
        
        
