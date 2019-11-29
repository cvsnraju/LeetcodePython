# 633. Sum of Square Numbers
# Easy

# Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

# Example 1:

# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5

class Solution:
  def judgeSquareSum(self, c: int) -> bool:
    """
    :type c: int
    :rtype: bool
    """
    a, b = 0, math.floor(math.sqrt(c))
    while a <= b:
      current_sum = a**2 + b**2
      if current_sum == c:
        return True
      elif current_sum > c:
        b -= 1
      else:
        a += 1
      return False