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

class Solution {
    
    public String longestCommonPrefix(String[] strs) {
        char[] lastInList = strs[strs.length-1].toCharArray();

        String compare = "";

        for (int i = 0; i < lastInList.length; i++) {
            compare += lastInList[i];
            
            for (int idx = 0; idx < strs.length; idx++) {
                char cArr = strs[idx].toCharArray();
                if (!strs[idx].contains(compare) && cArr[i].equals(compare)){
                    return compare.substring(0,compare.length()-1);
                }
                
            }
            
        }

        return compare.substring(0,compare.length()-1);
    }
}