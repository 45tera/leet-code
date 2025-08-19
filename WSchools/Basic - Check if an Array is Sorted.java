
/* 
++++++++++++++++++++++++++++
Qn: Given an array arr[], check if it is sorted in ascending order or not. Equal values are allowed in an array and two consecutive equal values are considered sorted.

Example 1:

Input: arr[] = [10, 20, 30, 40, 50]
Output: true
Explanation: The given array is sorted.

Input: arr[] = [90, 80, 100, 70, 40, 30]
Output: false
Explanation: The given array is not sorted.

++++++++++++++++++++++++++++
Breakdown:
1)  Iterative Appraoch
++++++++++++++++++++++++++++
Key Takeaways:
Storage of iteration is > Recursive.
*/

class Basic3 {

    public static void main(String[] args) {
        Integer[] a = { 10,20,30,40,50};
        Integer[] b = { 90,80,100,70,40,30};
        
        System.out.println(Check_if_Array_Sorted(a));
        System.out.println(Check_if_Array_Sorted(b));
    }

    public static String Check_if_Array_Sorted(Integer[] a) {

        for (int i = 0; i < a.length-2; i++) {
            if (a[i] > a[i+1]){
                return "false";
            }

        }
        
        return "true";
    }

}
