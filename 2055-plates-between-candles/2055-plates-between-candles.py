class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        '''Binary search O(N + QlogN)'''
        # A stores the indices of plates in 's'. 
        A = [i for i,c in enumerate(s) if c == '|']
        res = []
        print(A)
        for a,b in queries:
            i = bisect.bisect_left(A, a) # A[i] is the first index from 'a' to its right, where there's a plate
            j = bisect.bisect(A, b) - 1  # A[j] is the first index from 'b' to its left, where there's a plate
                          # bisect returns the index where b should be present in A, if b already exists in A, it returns next index to b in A, so we need to do -1 to get the right index
            
            # Let E be, No. of elements between plates at j & i = A[j] - A[i] + 1
            # Let P be, No. of plates between plates at j & i = j-i+1  (Since A stores indices of plates so if there's a plate between i & j, we'll  get it's count by j-i+1)
            # No. of candles = E-P => A[j] - A[i] + 1 - (j-i+1) = A[j] - A[i]) - (j - i)
            res.append((A[j] - A[i]) - (j - i) if i < j else 0)
        return res
        
        
        
        # n = len(s)
        # # print(n)
        # prefixSum, ans = [0]*n, []
        # for i in range(n): prefixSum[i] = prefixSum[i-1] + ( 1 if s[i]=='*' else 0)
        # # print(prefixSum)
        # for que in queries:
        #     left, right = que[0], que[1]
        #     while(left<right):
        #         if s[left] == '*': left+=1
        #         if s[right] == '*': right-=1
        #         if s[left] == '|' and s[right] =='|': break
        #     ans.append(prefixSum[right]-prefixSum[left] if left<=right else 0)
        # return ans