/* Soln: Myself

++++++++++++++++++++++++++++
Qn: Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
 
++++++++++++++++++++++++++++
Breakdown:
Traverse the array, from the back (reverse). Once a zero is detected, check from the reverse of the list to that 0 detected to shift the values again
++++++++++++++++++++++++++++
Key Takeaways:
- Arrays in Java, along with array.length() function, for loops in Java
- Too Much Time Spent
*/

class Solution {
    public void duplicateZeros(int[] arr) {
        for (int i = arr.length; i>0 ; i--){
            if (arr[i-1] == 0){
                for (int q = arr.length; q>i; q--){
                    arr[q-1] = arr[q-2];

                }
            }
            
        };   
    }
}
