class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_len, t_len = len(s), len(t)
        if s_len != t_len: return False
        freq_s, freq_t = collections.Counter(s), collections.Counter(t)
        return freq_s == freq_t
        # start, end, letter_count, ans = 0,0, 0, 0
        # t_len = len(t)
        # while(end < len(s)):
        #     if s[end] in t:
        #         letter_count+=1
        #     if end-start+1 < t_len:
        #         end+=1
        #     elif end-start+1 == t_len:
        #         if letter_count== t_len : ans+=1
        #         if s[start] in t: letter_count-=1
        #         end+=1
        #         start+=1
        # return ans