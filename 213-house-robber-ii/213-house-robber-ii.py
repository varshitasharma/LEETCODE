class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1: return nums[0]
        first = nums[:-1]
        last = nums[1:]
        # print(first, last)
        return max(self.helper(first), self.helper(last))
    def helper(self,arr):
        prev2, prev1 = 0,0
        for i in range(len(arr)):
            pick = arr[i] + prev2
            notPick = prev1
            prev2, prev1 = prev1, max(pick, notPick)
        return prev1
        