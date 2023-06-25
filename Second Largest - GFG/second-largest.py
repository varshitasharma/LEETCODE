#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
		# code here
		first, second =arr[0], -1
		for num in arr:
		    if num>first: 
		      first, second= num,first
	       # elif num==first: pass
		    elif num>second and num!=first : second = num
	    return second


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends