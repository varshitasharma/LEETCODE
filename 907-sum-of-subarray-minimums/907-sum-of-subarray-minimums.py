class Solution:
    '''https://leetcode.com/problems/sum-of-subarray-minimums/discuss/178876/stack-solution-with-very-detailed-explanation-step-by-step'''
    '''O(N)'''
    def sumSubarrayMins(self, arr: List[int]) -> int:
        #PLE- Previous Less Element, NLE - Next Less Element
        n, ans, mod = len(arr), 0, 1e9+7
        PLE, NLE = [-1]*n, [n]*n
        stackP, stackN = [], []
        for i, num in enumerate(arr):
            while(stackP and num <= arr[stackP[-1]]):
                stackP.pop()
            PLE[i] = stackP[-1] if stackP else  -1
            stackP.append(i)
        for i in range(n-1, -1, -1):
            while(stackN and arr[stackN[-1]] > arr[i] ):
                stackN.pop()
            NLE[i] = stackN[-1] if stackN else n
            stackN.append(i)
        for i in range(n):
            ans += (arr[i]*((i-PLE[i])*(NLE[i]-i)))%mod  #i-PLE[i] gives no. of elements from i to it's left till where arr[i] is minimum. Similarly for i -PLE[i] on the right side.
            # Product of both left*right gives the number of subarrays for which arr[i] is minimum.
        return int(ans%mod)
            
            