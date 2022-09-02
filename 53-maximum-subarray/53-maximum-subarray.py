class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ, maxx = 0, -float('inf')
        for i in range(len(nums)):
            summ += nums[i]
            if maxx < summ : maxx = summ
            if summ < 0: summ = 0
            
        return maxx
        
        # dp = [*nums]
        # # print(dp)
        # for i in range(1, len(nums)):
        #     dp[i] = max(nums[i], nums[i] + dp[i-1])
        #     # print(dp)
        # return max(dp)