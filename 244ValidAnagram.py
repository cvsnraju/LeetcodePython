# 242. Valid Anagram
# Easy
# Given two strings s and t , write a function to determine if t is an anagram of s.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        for item in s:
            if item not in d:
                d[item] = 1
            else:
                d[item] += 1
        for item in t:
            if item in d:
                d[item] -= 1
            else:
                return False
        for key, value in d.items():
            if value != 0:
                return False 
        return True 
        