class Solution:
    '''O(N^2) with O(1) space
    In total, 2n-1 centers are possible fpr all possible palindromes& to check each it'll take O(N time)'''
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s, l, r):
        while 0<=l <= r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]
    
    
    '''O(N^2) with O(N*N) space
    https://leetcode.com/problems/longest-palindromic-substring/discuss/900639/Python-Solution-%3A-with-detailed-explanation-%3A-using-DP'''
    
#     def longestPalindrome(self, s):
#         longest_palindrom = ''
#         dp = [[0]*len(s) for _ in range(len(s))]
#         #filling out the diagonal by 1
#         for i in range(len(s)):
#             dp[i][i] = True
#             longest_palindrom = s[i]
			
#         # filling the dp table
#         for i in range(len(s)-1,-1,-1):
# 				# j starts from the i location : to only work on the upper side of the diagonal 
#             for j in range(i+1,len(s)):  
#                 if s[i] == s[j]:  #if the chars mathces
#                     # if len slicied sub_string is just one letter if the characters are equal, we can say they are palindomr dp[i][j] =True 
#                     #if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
#                     if j-i ==1 or dp[i+1][j-1] is True:
#                         dp[i][j] = True
#                         # we also need to keep track of the maximum palindrom sequence 
#                         if len(longest_palindrom) < len(s[i:j+1]):
#                             longest_palindrom = s[i:j+1]
                
#         return longest_palindrom