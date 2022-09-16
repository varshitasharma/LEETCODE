class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # q = deque() # stores *indices*
        # res = []
        # for i, cur in enumerate(nums):
        #     while q and nums[q[-1]] <= cur:
        #         q.pop()
        #     q.append(i)
        #     # remove first element if it's outside the window
        #     if q[0] == i - k:
        #         q.popleft()
        #     # if window has k elements add to results (first k-1 windows have < k elements because we start from empty window and add 1 element each iteration)
        #     if i >= k - 1:
        #         res.append(nums[q[0]])
        # return res
        
        
        q, start, end, l, output = [], 0, 0, len(nums), []
        heapify(q)
        while(end < l):
            heappush(q,(-nums[end], end))
            if end-start+1 <k: end+=1
            elif end-start+1 == k:
                output.append(-q[0][0])
                # if start+1>q[0][1]: heappop(q)
                while( q and start+1>q[0][1]): heappop(q)
                end+=1
                start+=1
        return output
                
                    
        