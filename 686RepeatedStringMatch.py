# 686. Repeated String Match
# Easy

# Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

# For example, with A = "abcd" and B = "cdabcdab".

# Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

class Solution:
  def repeatedStringMatch(self, A: str, B: str) -> int:
    i = 0
    s = ''
    if set(A).issubset(set(B)):
      while len(s) <= len(A) + len(B):
        if B in s:
            break
        i += 1
        s += A         
    if B in s:
      return i
    elif len(s) == 0:
      s = A
      if B in s:
        return 1
    return -1 
    