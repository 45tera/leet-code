"""
The Problem: Given an array of integers, move all 0's to the end of it while maintaining the relative order of the non-zero elements. You must do this in-place without making a copy of the array.

Example:

Input: [0, 1, 0, 3, 12]

Desired Output: [1, 3, 12, 0, 0]
"""

"""
Strategy 1 - Bubble Sort ish
[1,0,0,3,12] -> swap again [1,0,0,3,12] + check the "safe area 1,0; yeah. 0 is at the end."->  swap again [1,0,3,0,12] + check safe area from the back 1,0,3. swap the 0 and 3. [1,3,0,0,12] -> swap again [1,3,0,12,0] + check safe area from the back 1,3,0,12. swap 0 and 12. [1,3,12,0,0]
"""
def move_zeros_strat1(nums):
   
    for i in range(1,len(nums)):
        j = i -1;
        while j >= 0 and nums[j] == 0: 
            right_val = nums[j+1]
            nums[j+1] = nums[j]
            nums[j] = right_val
            j-=1 # backtracking by going from index j, which is the "pointer" the the "safe area" to 0.
    return nums

"""
Due to the nature of the nested component, its a O(n^2) compexity. Space wise, its in-place, so its O(n). 
Not the worst. 
"""

"""
Strategy 2 - Swap on find, kinda like insertion sort
[0,1,0,3,12] -> do like an insertion sort using two pointer. have one pointer at the first zero, and if the moment we find the next non zero value, we swap it.
[1,3,0,0,12] -> [1,3,12,0,0]

"""

def move_zeros_strat2(nums):
    last_non_zero = -1
    last_zero = -1
    for i in range(0, len(nums)):
        if (nums[i] == 0 and last_zero== -1):
            last_zero = i 
        elif (nums[i] != 0):
            last_non_zero =i
            if last_zero != -1:
                nums[last_zero] = nums[i]
                nums[i] = 0
                last_zero +=1 #assisted. "safe zone+1"
                
        
    return nums
  

"""
I just realised to add in, there will be amortised doubling on the space. Shucks.
"""

"""
AI suggested answer is super short. I like it!
"""
def move_zeros_AI(nums):
    i = 0  
    for j in range(len(nums)):
        if nums[j] != 0: 
            nums[i], nums[j] = nums[j], nums[i] 
            i += 1 
