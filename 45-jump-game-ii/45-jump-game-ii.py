class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        '''O(N) Greedy'''
        curEnd, l, farthest, jumps = 0, len(nums), 0, 0
        # Current end is the last index you can go 
        for i in range(l-1):
            farthest = max(farthest, i+nums[i]) # Update farthest you can reach from any index
            if i == curEnd:                     # While iterating, once you reach curEnd, update CurEnd with the farthest                         
                jumps+=1                        #that you could reach till now and increment jump bcz now you have to jump to next curEnd
                curEnd = farthest
        return jumps
    
    
        '''O(N^2) DP'''
        # l, last = len(nums),0
        # min_jumps = [float('inf')]*l
        # min_jumps[0] = 0
        # for i in range(l):
        #     if i<= last and last <nums[i]+i:
        #         # if last <nums[i]+i:
        #         for index in range(i+1, min(l, nums[i]+i+1)):
        #             min_jumps[index] = min(min_jumps[index], min_jumps[i]+1)
        #         last = nums[i]+i
        # return min_jumps[-1]
        