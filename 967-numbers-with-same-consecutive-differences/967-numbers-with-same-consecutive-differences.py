class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        q = deque((1,digit) for digit in [1,2,3,4,5,6,7,8,9]) # Append all possible 1 digit numbers to queue as                                                                   tuple(length of num, num)
        output = []
        while(q):
            length, num = q.popleft()  # if length of num == required length then append to result
            if length == n: output.append(num)
            else:
                for digit in range(10): # check for each possible next digit if difference between last digit of num
                                        # and next digit is == k
                    if abs(num%10 - digit) == k: q.append((length+1, num*10 + digit)) # if yes then add that digit to last of                                                                                       #current number and append it to q 
        return output
                        
                