# 507. Perfect Number
# We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
# Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.

# Example:

# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
from math import sqrt
class Solution:
    def checkPerfectNumber(self, num: int) -> bool :
        s = 1
        if num == 1:
            return False
        l = int(sqrt(num))
        for k in range(2,l+1):
            if num%k == 0:
                s = s + num/k + k
            elif num/k == k:
                s = s - k
        if s == num:
            return True
        else:
            return False
res = Solution().checkPerfectNumber(81)
print(res)
