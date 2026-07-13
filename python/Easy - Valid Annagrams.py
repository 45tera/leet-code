"""
++++++++++++++++++++++++++++
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
++++++++++++++++++++++++++++
"""
         
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) == len(t):
            # Put here is important - immediate garbage collection on placing it before the if condition IF the check condition fails
            dict1 = {}
            dict2 = {}
            for char in s:
                dict1[char] = dict1.get(char,0) +1
            for char in t:
                dict2[char] = dict2.get(char,0) +1
        
            return dict1 == dict2 # Collections.counter is better.
        return False

# I think its interesting to think about, cause like is question's solution (or the main use of the dictionary) will be capped at O(N), given that this question is set in English. 
# If the character inputs allowed for Unicode, our O(N), or O(K), will be the max number of Unicode characters out there, making it more than O(1) if we dont know the exact number lol, but could increase more.
# However, in the end, O(K) for K distinct characters is still bounded by O(N) because a string of N can only go as much as N. So. O(K) is not very much slower than O(N)


"""
NeetCode Retry 
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_1 = {}
        dict_2 = {}
        for index in range(len(s)): #doesn matter cus they same 
            dict_1[s[index]] = dict_1.get(s[index],0) +1
            dict_2[t[index]] = dict_2.get(t[index],0) +1
        
        return dict_1 == dict_2
        
