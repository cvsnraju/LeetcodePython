# Given an integer, write a function to determine if it is a power of three.
# Example 1:
# Input: 27
# Output: true
# Example 2:
# Input: 0
# Output: false
# Example 3:
# Input: 9
# Output: true


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        i = 1
        while i < n:
            i = i*3
        return i == n
        