/*
++++++++++++++++++++++++++++
Qn: Given an array nums of integers, return how many of them contain an even number of digits.
Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.

Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
++++++++++++++++++++++++++++
Breakdown:
Use the /10 to access one digit by one digit; and then % to check if even or odd.
++++++++++++++++++++++++++++
Key Takeaways:
- Be careful when using comparison operators. One test case was when [100000] was placed, and the resulting number was 10, so the last digit is not counted as my loop only considered numbers bigger than 10 and not exactly 10.

*/

int findNumbers(int* nums, int numsSize) {
    int even = 0;

    for (int i=0; i < numsSize; i++){
        int number = nums[i];
        int noDigits = 1;
        
        if (number > 10){
            while (number >= 10){
                number = number / 10;
                noDigits++;
            }
            
            if (noDigits % 2 == 0){ /*when noDigits*/
                even++;
            }
            
        }
            
        
        
        
    }

    return even;

}

