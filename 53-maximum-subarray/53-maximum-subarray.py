class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        dp = [*nums]
        # print(dp)
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
            # print(dp)
        return max(dp)