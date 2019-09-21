import copy
lst = ['a', [1, 2], ['b', [2, 'c']], 'd']
lst_copy = copy.copy(lst)
lst_copy[0] = 'A'
lst_copy[1][1] += 10
lst_copy[2][1][0] *= 4
print(lst)
print(lst_copy)

import copy
lst = ['a', [1, 2], ['b', [2, 'c']], 'd']
lst_deepcopy = copy.deepcopy(lst)
lst_deepcopy[0] = 'A'
lst_deepcopy[1][1] += 10
lst_deepcopy[2][1][0] *= 4
print(lst)
print(lst_deepcopy)
