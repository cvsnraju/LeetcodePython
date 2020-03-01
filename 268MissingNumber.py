class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    for k in range(len(nums)):
      if k not in nums:
        return k
    return len(nums)