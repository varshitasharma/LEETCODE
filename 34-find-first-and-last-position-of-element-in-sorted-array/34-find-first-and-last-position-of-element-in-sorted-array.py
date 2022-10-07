class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        while(left<=right):
            mid = (left+right)//2
            # print(mid)
            if nums[mid] == target:
                leftmid = bisect.bisect_left(nums[:mid], target)
                rightmid = mid + bisect.bisect(nums[mid:], target) -1
                return [leftmid, rightmid]
            elif nums[mid]>target: right = mid-1
            else: left = mid+1
        return [-1,-1]
                