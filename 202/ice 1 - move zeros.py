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
  




"""
Strategy 2 - Swap on find, kinda like insertion sort
[1,0,0,3,12] -> do like an insertion sort using two pointer. have one pointer at the first zero, and if the moment we find the next non zero value, we swap it.
[1,3,0,0,12] -> [1,3,12,0,0]

"""

def move_zeros_strat2(nums):
  
