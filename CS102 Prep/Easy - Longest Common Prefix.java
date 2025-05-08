/*
++++++++++++++++++++++++++++
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
++++++++++++++++++++++++++++
Breakdown:
1. 
++++++++++++++++++++++++++++
Key Takeaways:
- 
 */

import java.util.*;

class Solution {
    
    public String longestCommonPrefix(String[] strs){
        String shortestWord = strs[0];
        ArrayList<String> m = new ArrayList<>();

        for (String s: strs){
            m.add(s);
            if(s.length() < shortestWord.length()){
                shortestWord = s;
                m.remove(s);
            }
        }
        
        
        String compare ="";
        char[] cArr = shortestWord.toCharArray();

        
        
        for (int i =0; i < cArr.length ; i++){
            compare+= cArr[i];
            
            for (int x = 0; x < m.size(); x++){
                
            }
            
        }
        
        return compare.substring(0,compare.length()-1);
    }
}