class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l, last = len(nums), 0
        for i in range(l):
            if last >l-2: return True
            if i<=last:
                if nums[i] + i>last : last=  nums[i] + i
        return False
        
            