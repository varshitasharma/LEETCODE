class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        q = deque((1,digit) for digit in [1,2,3,4,5,6,7,8,9])
        output = []
        while(q):
            length, num = q.popleft()
            if length == n: output.append(num)
            else:
                for digit in range(10):
                    if abs(num%10 - digit) == k: q.append((length+1, num*10 + digit))
        return output
                        
                