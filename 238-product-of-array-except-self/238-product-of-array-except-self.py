class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        left, right,ans = [1]*l, [1]*l, [1]*l
        left[0], right[l-1] = nums[0], nums[l-1]
        for i in range(1, l):
            left[i] = left[i-1]*nums[i]
        for i in range(l-2, -1,-1):
            right[i] = right[i+1]*nums[i]
        # print(left, right)
        for k in range(1,l-1):
            ans[k] = left[k-1]*right[k+1] 
        ans[0], ans[l-1] = right[1], left[l-2]
        return ans