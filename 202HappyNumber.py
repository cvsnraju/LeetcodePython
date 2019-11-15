
# 202. Happy Number
# Easy

# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, 
# replace the number by the sum of the squares of its digits, 
# and repeat the process until the number equals 1 (where it will stay), 
# or it loops endlessly in a cycle which does not include 1. 
# Those numbers for which this process ends in 1 are happy numbers.

class Solution:
  def isHappy(self, n: int) -> bool:
      
    dic = {}
    
    def happy(num, dic):
    
      lst = [int(x) for x in str(num)]
  
      s = 0
  
      for x in lst:
        s = s + x*x
  
      if s == 1:
        return True
      elif s in dic:
        return False
      else:
          dic[s] = 1
        return happy(s, dic)
    
      return happy(n, dic)
                
        
        