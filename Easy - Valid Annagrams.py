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


