class Solution:
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
            # print(stackN)
            while(stackN and arr[stackN[-1]] > arr[i] ):
                stackN.pop()
            NLE[i] = stackN[-1] if stackN else n
            stackN.append(i)
        # PLE[0], NLE[n-1] = -1, n
        # print(NLE,PLE)
        for i in range(n):
            # left = (i-PLE[i] if i!=PLE[i] else 1)
            # right = (NLE[i]-i if i!=NLE[i] else 1)
            ans += (arr[i]*((i-PLE[i])*(NLE[i]-i)))%mod
            # print(ans)
        return int(ans%mod)
            
            