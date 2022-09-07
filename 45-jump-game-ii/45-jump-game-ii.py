class Solution:
    def jump(self, nums: List[int]) -> int:
        l, last = len(nums),0
        min_jumps = [float('inf')]*l
        min_jumps[0] = 0
        for i in range(l):
            if i<= last:
                if last <nums[i]+i:
                    for index in range(i+1, min(l, nums[i]+i+1)):
                        min_jumps[index] = min(min_jumps[index], min_jumps[i]+1)
                    last = nums[i]+i
        return min_jumps[-1]