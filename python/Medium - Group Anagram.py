"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finalDict = {}
        for word in strs:
            keyList = sorted(word)
            key = "".join(keyList) # technically could mash into one line, with above. but readability would be not fun

            if key not in finalDict:
                finalDict[key] = []
            finalDict[key].append(word)
        
        return list(finalDict.values())
        

# Cool thing I learnt today was my first guess on this was to use ASCII to calculate, the similarity among them was actually causing a collusion which I didnt see at all at the start.
# Python uses Timsort!
