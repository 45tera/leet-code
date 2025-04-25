/*
++++++++++++++++++++++++++++
Given an integer x, return true if x is a palindrome, and false otherwise.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
++++++++++++++++++++++++++++
Breakdown:
1. 
++++++++++++++++++++++++++++
Key Takeaways:
-  != (compares memory location)
-  Usage of mod to extract the digits, and Collections.reverse()

 */

import java.util.*;

class Solution {

    // bruteforce method - 49ms
    // public boolean isPalindrome(int x) {
    //     String strX = String.valueOf(x);
    //     String[] arrX =  strX.split("");
    //     System.out.println(arrX);
    //     for (int i = arrX.length; i>0; i--){
    //         if (!arrX[arrX.length - i].equals(arrX[i-1])){
    //             return false;   
    //         }
    //     }
    //     return true;
    // }

    // 10ms
    public boolean isPalindrome(int x) {
        if (x < 0){
            return false;
        }

        ArrayList<Integer> o = new ArrayList<>();

        while (x > 0) {
            o.add(0, x % 10); 
            x /= 10;
        }
        ArrayList<Integer> mo = new ArrayList<>(o);        
        Collections.reverse(mo);

        return mo.equals(o);
    }


}