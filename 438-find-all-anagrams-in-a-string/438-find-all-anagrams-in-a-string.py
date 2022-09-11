class Solution(object):
    def findAnagrams(self, s, t):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        letter_count_t = collections.Counter(t)
        start, end, ans,  letter_count = 0,0, [], collections.Counter('')
        t_len = len(t)
        while(end < len(s)):
            if s[end] in t:
                letter_count[s[end]]= letter_count[s[end]]+1
            if end-start+1 < t_len:
                end+=1
            elif end-start+1 == t_len:
                if letter_count== letter_count_t : ans.append(start)
                if s[start] in t: letter_count[s[start]]-=1
                end+=1
                start+=1
        return ans