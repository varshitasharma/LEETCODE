class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ''' *** Without using Bisect python fxn****
        
        
        public int[] searchRange(int[] nums, int target) {
        double left = target - 0.5, right = target + 0.5;
        #Search for element 0.5 less than target gives the index of number just greater than target or target itself(if present)
        #Search for element 0.5 greater than target gives the index of number just greater than target
        int l = bs(nums, left), r = bs(nums, right);
        # if target isn't present in the list, l will be equal to r
        if(l == r) return new int[]{-1, -1};
        # if target is present, l won't be equal to r & since r = index of number just greater than target, do r=r-1
        return new int[]{l, r-1};
}
    
public int bs(int[] nums, double target) {
        int l = 0, h = nums.length-1;
        while(l <= h){
            int m = l + (h - l)/2;
            if(target > nums[m]) l = m+1;
            else h = m-1;
        }
        return l;
}
        '''
        
        
        
        
        # *** Without using Bisect python fxn****
        
        
        def search(n):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] >= n:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        lo = search(target)
        return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1, -1]
# Here, my helper function is a simple binary search, telling me the first index where I could insert a number n into nums to keep it sorted. Thus, if nums contains target, I can find the first occurrence with search(target). I do that, and if target isn't actually there, then I return [-1, -1]. 
# Otherwise, I ask search(target+1), which tells me the first index where I could insert target+1, which of course is one index behind the last index containing target, so all I have left to do is subtract 1.
        
        
        
        # left, right = 0, len(nums)-1
        # while(left<=right):
        #     mid = (left+right)//2
        #     # print(mid)
        #     if nums[mid] == target:
        #         #this returns the leftmost index of target using binary search
        #         leftmid = bisect.bisect_left(nums[:mid], target)
        #         #this returns the rightmost index of target using binary search
        #         rightmid = mid + bisect.bisect(nums[mid:], target) -1
        #         return [leftmid, rightmid]
        #     elif nums[mid]>target: right = mid-1
        #     else: left = mid+1
        # return [-1,-1]
                