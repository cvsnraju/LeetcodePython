# 561. Array Partition I
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        d = 0
        i = 0
        if len(nums) <= 2:
            return min(nums)
        y = len(nums) // 2
        nums.sort()
        for k in range(y):
            d = d + min(nums[i],nums[i+1])
            i+=2
        return d