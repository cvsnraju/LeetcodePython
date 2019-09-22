def HouseRobber(nums):
    if len(nums) <= 1 :
        return nums
    dp = [0]*len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[1],nums[0])
    for k in range(2,len(nums)):
        dp[k] = max(nums[k] + dp[k-2], dp[k-1])
    return 'largest sum can be robbed is: {0}'.format(dp[-1])
res = HouseRobber([2,1,1,2])
print(res)