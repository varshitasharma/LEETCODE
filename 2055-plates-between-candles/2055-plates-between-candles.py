class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        '''O(N + Q)'''
        '''
        For each indice, find the nearest candle index on the left and on the right.

Example:

                        0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20

                        *  *  *  |  *  *  |  *  *  *   *   *   |   *   *   |   |   *   *   |   *
nearest right candle:   3  3  3  3  6  6  6  12 12 12  12 12  12  15  15  15   16  19  19  19  -
nearest left candle:    -  -  -  3  3  3  6  6  6  6   6  6   12  12  12  15  16  16  16   19  19
candle count:           0  0  0  1  1  1  2  2  2  2   2  2    3   3   3   4   5   5   5   6   6
        '''
        
        n = len(s)
        nearLeft, nearRight= [-1]*n,[-1]*n
        candleCount, res = [0]*n, []   #candleCount[i] stores no. of candles till index i
        
        candle = -1   #no candle found yet
        for i in range(n-1,-1,-1):
            if s[i] == '|': 
                candle = i
            nearRight[i] = candle
            
        candle, count = -1,0
        for i in range(0,n):
            if s[i] == '|': 
                candle = i
                count+=1
            nearLeft[i] = candle
            candleCount[i] = count
       
        for a,b in queries:
            left, right = nearRight[a], nearLeft[b]
            if left==-1 or right==-1 or left>=right : res.append(0)
            else: res.append(right-left - (candleCount[right]-candleCount[left]) )
        return res
        
        
        
        '''Binary search O(N + QlogN)'''
#         # A stores the indices of plates in 's'. 
#         A = [i for i,c in enumerate(s) if c == '|']
#         res = []
#         print(A)
#         for a,b in queries:
#             i = bisect.bisect_left(A, a) # A[i] is the first index from 'a' to its right, where there's a plate
#             j = bisect.bisect(A, b) - 1  # A[j] is the first index from 'b' to its left, where there's a plate
#                           # bisect returns the index where b should be present in A, if b already exists in A, it returns next index to b in A, so we need to do -1 to get the right index
            
#             # Let E be, No. of elements between plates at j & i including i,j= A[j] - A[i] + 1
#             # Let P be, No. of plates between plates at j & i including plates at j&i= j-i+1  (Since A stores indices of plates so if there's a plate between i & j, we'll  get it's count by j-i+1)
#             # No. of candles = E-P => A[j] - A[i] + 1 - (j-i+1) = A[j] - A[i]) - (j - i)
#             res.append((A[j] - A[i]) - (j - i) if i < j else 0)
#         return res
        
        
        
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