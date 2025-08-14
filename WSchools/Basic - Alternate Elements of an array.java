import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

/* Soln: Myself

++++++++++++++++++++++++++++
Qn: Given an array arr[], the task is to print every alternate element of the array starting from the first element.

Example 1:

Input: arr[] = [10, 20, 30, 40, 50]
Output: 10 30 50
Explanation: Print the first element (10), skip the second element (20), print the third element (30), skip the fourth element(40) and print the fifth element(50).

Input: arr[] = [-5, 1, 4, 2, 12]
Output: -5 4 12

++++++++++++++++++++++++++++
Breakdown:
1) Iterative Approach - for loop with i+2 as the iteration to print; - O(n)
2) Recursive -
++++++++++++++++++++++++++++
Key Takeaways:

*/

class Basic1 {

    public static void main(String[] args) {
        String[] a = { "10", "20", "30", "40", "50" };
        Queue<String> q = new LinkedList<>(Arrays.asList(a));
        Alternate_Elements(q);
    }

    public static String Alternate_Elements(Queue<String> q) {

        while(q.size() >= 1){
            System.out.println(q.peek());

            q.remove();
            q.remove();

        
            return Alternate_Elements(q);
        }
            
        return "Finished";
    }

        
}
