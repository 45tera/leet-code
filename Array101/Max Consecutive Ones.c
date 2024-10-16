/* Soln: rajdipsaha-IIT-KGP 

++++++++++++++++++++++++++++
Qn: Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
++++++++++++++++++++++++++++
Breakdown:
Traverse the array, window by window. Whenever 0 is encountered, the count resets.
++++++++++++++++++++++++++++
Key Takeaways:
- Arrays can only be initialized with curly braces on definition. After which, it is immutable 
    - See:https://stackoverflow.com/questions/22807427/cannot-convert-brace-enclosed-initializer-list
- Too Much Time Spent
*/

int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int streak=0;
    int count=0;
    for(int i=0;i<numsSize;i++)
    {
        if(nums[i]==1)
        {
            count++;
            if(count>=streak)
            streak=count;
        }
        else
        count=0;
    }
    return streak;
}
