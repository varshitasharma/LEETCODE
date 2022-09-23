class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        left, right, maxL, maxR, ans = [0]*l, [0]*l, 0, 0, 0
        for i in range(l):
            if maxL < height[i]: maxL = height[i]
            left[i] = maxL
        for j in range(l-1, -1, -1):
            if maxR < height[j]: maxR = height[j]
            right[j] = maxR
        for k in range(l):
            ans += min(left[k], right[k]) - height[k]
        return ans