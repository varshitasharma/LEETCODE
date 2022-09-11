class Solution(object):
    def findAnagrams(self, s, t):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        letter_count_t = collections.Counter(t) #store count of letters of pattern
        start, end, ans,  letter_count = 0,0, [], collections.Counter('')  # letter_count stores 0 for all letters by default
                                                                        # it'll be used to store occurrences of all letters in a window
        t_len = len(t)
        while(end < len(s)):
            if s[end] in t:   # update letter count if the letter is in pattern
                letter_count[s[end]]+=1
            if end-start+1 < t_len:
                end+=1
            elif end-start+1 == t_len:  #when window length achieved 
                if letter_count== letter_count_t : ans.append(start)  #if Counter of the actual matches with Counter of substring in current window
                if s[start] in t: letter_count[s[start]]-=1   #before moving the window check if the start index(which will be out of window as window moves) contributes to letter count. If yes then decrease the letter count of that letter by 1
                end+=1
                start+=1
        return ans