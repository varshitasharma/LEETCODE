class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx, cur = 0,0
        for num in nums:
            if num == 1: cur+=1
            else:
                maxx = max(maxx, cur)
                cur = 0
        return max(maxx, cur)
            