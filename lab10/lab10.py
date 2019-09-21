#Problem 1
from ChainingHashTableMap import ChainingHashTableMap,print_hash_table

def list_intersection(lst1, lst2):
    table = ChainingHashTableMap()
    lst = []
    for i in lst1:
        table[i] = 1
    for j in lst2:
        try:
            table[j]
            lst.append(j)
        except:
            continue
    return lst
lst1 = [5,6,1,10]
lst2 = [8,1,9,5,3,8]
#print(list_intersection(lst1,lst2))

#Problem 2
## average & worst-case runtime O(n)
def mode_of_list(lst):
    table = ChainingHashTableMap()
    most = (0,0) ##(key,appearance)
    for i in lst:
        try:
            table[i] += 1
            if table[i] > most[1]:
                most = (i,table[i])
        except:
            table[i] = 0
    return most[0]
lst = [1, 3, 2, 1, 2, 1]
#print(mode_of_list(lst))

#Problem 3
## binarysearchtreemap
def two_sum(lst,target):
    table = ChainingHashTableMap()
    for i in range(len(lst)):
        num = lst[i]
        table[num] = i
        need = target - num
        try:
            loc = table[need]
            return loc,i
        except:
            pass
    return (None,None)
lst = [-5, 2, 8, -3, 7, 1]
#print(two_sum(lst,-1))

#Problem 4
def is_anagram(str1, str2):
    table = ChainingHashTableMap()
    for i in str1:
        try:
            table[i] += 1
        except:
            table[i] = 1
    for j in str2:
        try:
            table[j] -= 1
            if table[j] == 0:
                del table[j]
        except:
            #print_hash_table(table)
            return False
    return table.is_empty()

str1 = "enraged"
str2 = "angered"
#print(is_anagram(str1,str2))
            










    
