class Solution:
    def trap(self, height: List[int]) -> int:
        '''O(N) time & O(N) space'''
        # l = len(height)
        # left, right, maxL, maxR, ans = [0]*l, [0]*l, 0, 0, 0
        # for i in range(l):
        #     if maxL < height[i]: maxL = height[i]
        #     left[i] = maxL
        # for j in range(l-1, -1, -1):
        #     if maxR < height[j]: maxR = height[j]
        #     right[j] = maxR
        # for k in range(l):
        #     ans += min(left[k], right[k]) - height[k]
        # return ans
        
        '''O(N) time & O(1) space'''
        left, right, maxLeft, maxRight, ans = 0, len(height)-1, 0, 0, 0
        while(left < right):
            if height[left] < height[right]:
                if maxLeft <= height[left]: maxLeft = height[left]
                else: ans += maxLeft - height[left]
                left+=1
            else:
                if maxRight <= height[right]: maxRight = height[right]
                else:  ans+= maxRight - height[right]
                right-=1
        return ans