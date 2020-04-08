class Solution:
  def findRelativeRanks(self, nums: List[int]) -> List[str]:
    num = sorted(nums, reverse = True)
    L = {}
    medal = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    for i in range(len(nums)):
      if i < 3:
        L[num[i]] = medal[i]
      else:
        L[num[i]] = str(i+1)
    for j in range(len(nums)):
      nums[j] = L[nums[j]]
    return nums
            
        