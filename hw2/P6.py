#Question 6
from ArrayStack import ArrayStack

def eval_postfix_boolean_exp(boolean_exp_str):
    lst = boolean_exp_str.split()
    stack = ArrayStack()
    for i in lst:
        if i.isdigit():
            stack.push(int(i))
        else:
            second = stack.pop()
            first = stack.pop()
            if i == "<":
                new = first < second
            elif i == ">":
                new = first > second
            elif i == "&":
                new = first and second
            elif i == "|":
                new = first or second
            stack.push(new)
    answer = stack.pop()
    return answer

##s = "1 2 < 6 3 < |"
##print(eval_postfix_boolean_exp(s))
    
