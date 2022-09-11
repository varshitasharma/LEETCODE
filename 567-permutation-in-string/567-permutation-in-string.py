class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        letter_count, letter_count_s1, start, end, len_s1 = collections.Counter(''), collections.Counter(s1), 0, 0, len(s1)
        
        while(end<len(s2)):
            if letter_count_s1[s2[end]] > 0:
                letter_count[s2[end]]+=1
            if end-start+1 < len_s1:
                end+=1
            elif end-start+1 == len_s1:
                if letter_count == letter_count_s1: return True
                if letter_count_s1[s2[start]] > 0: letter_count[s2[start]]-=1
                start+=1
                end+=1
        return False