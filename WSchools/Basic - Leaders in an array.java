import java.util.ArrayList;

/* Soln: Myself

++++++++++++++++++++++++++++
Qn: Given an array arr[] of size n, the task is to find all the Leaders in the array. An element is a Leader if it is greater than or equal to all the elements to its right side.
Example 1:

Input: arr[] = [16, 17, 4, 3, 5, 2]
Output: [17 5 2]
Explanation: 17 is greater than all the elements to its right i.e., [4, 3, 5, 2], therefore 17 is a leader. 5 is greater than all the elements to its right i.e., [2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.

Input: arr[] = [1, 2, 3, 4, 5, 2]
Output: [5 2]
Explanation: 5 is greater than all the elements to its right i.e., [2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.

++++++++++++++++++++++++++++
Breakdown:
1)  Nested Loops - O(n^2)
2)
++++++++++++++++++++++++++++
Key Takeaways:
Nested Loops
a.length => returns exact size.
*/

class Basic2 {

    public static void main(String[] args) {
        Integer[] a = { 16, 17, 4, 3, 5, 2 };
        
        System.out.println(Leaders_in_an_array(a));
    }

    public static ArrayList<Integer> Leaders_in_an_array(Integer[] a) {

        ArrayList <Integer> result = new ArrayList<Integer>();

        int aRealLength = a.length; //exact size

        for (int i = 0; i < a.length; i++) {
            int j;
            for (j = i+1; j < a.length; j++) {
               
               if (a[i] < a[j]){
                   break;
               }
                
            }
            if (j == aRealLength && !result.contains(a[i])){
                result.add(a[i]);
            }

        }
        
        return result;
    }

}
