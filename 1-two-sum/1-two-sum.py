class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        for i, num in enumerate(nums):
            if target-num in pos:
                return [pos[target-num],i]
            pos[num] = i
        