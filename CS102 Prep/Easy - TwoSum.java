
import java.util.HashMap;

/*
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
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
++++++++++++++++++++++++++++
Breakdown:
1. O(n2) -> Use of the difference, nest loop to check the subsequent numbers are the same as the difference. Else, nothing is returned.
2. O(n) -> Use hashmap (index of number: difference from target), compute the difference.Store the difference in hashmap. For every number, check if the difference number exists in hashmap. returns the current index, and the index of the number with the same difference.
++++++++++++++++++++++++++++
Key Takeaways:
- Arrays.length to call upon. 
 */

 class Solution { 
    
    // O(n2) solution
    public int[] twoSum(int[] nums, int target) {
        
        for (int i=0; i < nums.length;i++){
            int diff = target - nums[i];

            for (int x = i+1; x < nums.length; x++){
                if (diff ==  nums[x]){
                    return new int[]{i, x};
                }
            }
        }
        return new int[]{};
    }

    // O(n)
    // Uses hashmap to map the complement, based on the concept of using the hash collision.
    public int[] twoSum_On(int[] nums, int target) {
        HashMap<Integer,Integer> mapList = new HashMap<>();
        Integer value = null;

        for (int i = 0; i < nums.length; i++) { //Iterating -> O(n)
            int pointerNumb = nums[i]; //searching - indexing -> O(1)
            int complement = target - pointerNumb; 
            
            if (i == 0){
               value = mapList.get(complement); //indexing for hashmap -> O(1) 
            }
            else{
                value = mapList.get(pointerNumb);
            }
            
            if (value != null){
                return new int[]{i, value};
            }else{
                mapList.put(complement, i);
            }

        }
        return new int[]{};
    }


}