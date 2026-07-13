"""
++++++++++++++++++++++++++++
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
++++++++++++++++++++++++++++
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diffDict = {}
        for curr_index, curr_number in enumerate(nums):
            diff = target - curr_number
            if curr_number in diffDict:
                return [diffDict[curr_number],curr_index]
            diffDict[diff] = curr_index
                

# Today's interesting learning was guard clause cases (reduce the mental strain on the increased indentation) + the use of enumerate in python.
#
# Also hit on an issue while coding this out - an unhashable type. So turns out that python hashes any data that is trying to do a search/comparison.
# But only immutable types in python are hashable, which make sense - like if a List was first hashed, and then the user adds in one more value, the hash of the entire List is going to change.
# So, how do mutable types get hashed?
#

        
        
