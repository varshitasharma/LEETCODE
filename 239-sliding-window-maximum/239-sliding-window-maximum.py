class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
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
                
                    
        