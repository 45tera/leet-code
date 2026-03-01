#!/bin/python3

import math

def get_index(permutation):
    # Write your code here
    no_slots = len(permutation) -1
    result = 0
    sorted_list = permutation.copy()
    sorted_list.sort()
    
    i = 0
    while i < len(permutation):
        digit = permutation[i]
        no_smaller_than_digit = sorted_list.index(digit)
        
        calculation = (no_smaller_than_digit * math.factorial(no_slots))
        
        result = result + calculation
        
        sorted_list.remove(digit)
        i+=1        
        no_slots -=1

    return result

if __name__ == '__main__':
    permutation = list(map(int, input().strip().split()))
    print(get_index(permutation))


#################################
# interesting learning - takeaway is about using factorials to count up to see what was skipped
