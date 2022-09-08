class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curEnd, l, farthest, jumps = 0, len(nums), 0, 0
        for i in range(l-1):
            farthest = max(farthest, i+nums[i])
            if i == curEnd:
                jumps+=1
                curEnd = farthest
        return jumps
        