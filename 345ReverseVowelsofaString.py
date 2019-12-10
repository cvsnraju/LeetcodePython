# 345. Reverse Vowels of a String
# Easy

# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:

# Input: "hello"
# Output: "holle"

class Solution:
  def reverseVowels(self, s: str) -> str:
    stor = dict()
    v = {'a','e','i','o','u','A','E','I','O','U'}
    l = len(s)
    for k in range(l):
      if s[k] in v:
        stor[k] = s[k]  
    res = list(s)
    y = list(stor.keys())
    y.sort()
    i = -1
    for p in range(len(y)):
      fi= stor[y[p]]
      res[y[p]] = stor[y[i]]
      res[y[i]] = fi
      i -= 1
        
    return "".join(res)
            
            
        
        