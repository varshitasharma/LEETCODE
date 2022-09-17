class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''Using Monotonic Queue TC: O(N)'''
        '''Store elements in the monotonic queue in decreasing order, so that the first elemet in the queue will be the maximum element of the current window. To maintain that, If current element in window (array) is larger than first element in queue keep popping and push the element when queue is empty or first elemet is the queue is larger than current element.'''
        q = deque() # stores *indices*
        res = []
        for i, cur in enumerate(nums):
            while q and nums[q[-1]] <= cur:
                q.pop()
            q.append(i)
            # remove first element if it's outside the window
            if q[0] == i - k:
                q.popleft()
            # if window has k elements add to results (first k-1 windows have < k elements because we start from empty window and add 1 element each iteration)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res
        
        '''Using MAX Heap TC: O(k*log(k)*N)'''
#         q, start, end, l, output = [], 0, 0, len(nums), []
#         heapify(q)
#         while(end < l):
#             heappush(q,(-nums[end], end))
#             if end-start+1 <k: end+=1
#             elif end-start+1 == k:
#                 output.append(-q[0][0])
#                 if q and start+1>q[0][1]: heappop(q)
#                 while( q and start+1>q[0][1]): heappop(q)
#                 end+=1
#                 start+=1
#         return output
                
                    
        