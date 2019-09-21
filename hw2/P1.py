#Question 1
import time
import random

class SimpleTimer:
    def __init__(self):
        self.start = time.time()

    def elapsed(self):
        return time.time() - self.start

    def reset(self):
        self.start = time.time()

def max_subsequence_sum1(lst):
    max_sum = 0
    start_seq = None
    end_seq = None
    for curr_start in range(len(lst)):
        for curr_end in range(curr_start, len(lst)):
            curr_sum = 0
            for i in range(curr_start, curr_end+1):
                curr_sum += lst[i]
            if curr_sum > max_sum:
                max_sum = curr_sum
                start_seq = curr_start
                end_seq = curr_end
    return max_sum, start_seq, end_seq


def max_subsequence_sum2(lst):
    max_sum = 0
    start_seq = None
    end_seq = None
    for curr_start in range(len(lst)):
        curr_sum = 0
        for curr_end in range(curr_start, len(lst)):
            curr_sum += lst[curr_end]
            if curr_sum > max_sum:
                max_sum = curr_sum
                start_seq = curr_start
                end_seq = curr_end
    return max_sum, start_seq, end_seq

def max_subsequence_sum3(lst):
    max_sum = 0
    start_seq = None
    end_seq = None

    curr_start = 0
    curr_sum = 0
    for curr_end in range(len(lst)):
        curr_sum += lst[curr_end]
        if curr_sum > max_sum:
            max_sum = curr_sum
            start_seq = curr_start
            end_seq = curr_end
        elif curr_sum < 0:
            curr_start = curr_end + 1
            curr_sum = 0
    return max_sum, start_seq, end_seq

##################
def make_random_lst(n):
    return [random.randint(-10000,10000) for i in range(n)]



my_timer = SimpleTimer()
lst = make_random_lst(2 ** 8)
my_timer.reset()
max_sum, start, end = max_subsequence_sum1(lst)
runtime = my_timer.elapsed()
##print(runtime)


my_timer = SimpleTimer()
my_timer.reset()
max_sum, start, end = max_subsequence_sum2(lst)
runtime = my_timer.elapsed()
##print(runtime)


my_timer = SimpleTimer()
my_timer.reset()
max_sum, start, end = max_subsequence_sum3(lst)
runtime = my_timer.elapsed()
##print(runtime)












