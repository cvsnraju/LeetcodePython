# 238. Product of Array Except Self
# Medium

# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    p = 1
    n = len(nums)
    output = []
    for i in range(0,n):
      output.append(p)
      p = p * nums[i]
    p = 1
    for i in range(n-1,-1,-1):
      output[i] = output[i] * p
      p = p * nums[i]
    return output
            
        
        
        
        