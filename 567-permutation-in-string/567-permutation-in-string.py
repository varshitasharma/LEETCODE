class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        letter_count, letter_count_s1, start, end, len_s1 = collections.Counter(''), collections.Counter(s1), 0, 0, len(s1)
        # letter_count_s1 contains count of all characters in s1
        while(end<len(s2)):
            if letter_count_s1[s2[end]] > 0: # if current character is present is s1
                letter_count[s2[end]]+=1   # Increment count of that character for current window
            if end-start+1 < len_s1:
                end+=1
            elif end-start+1 == len_s1:
                if letter_count == letter_count_s1: return True   #  #if Counter of the actual matches with Counter of substring in current window -> the current substring is a permutation of s1
                if letter_count_s1[s2[start]] > 0: letter_count[s2[start]]-=1  #  #before moving the window check if the start index(which will be out of window as window moves) contributes to letter count. If yes then decrease the letter count of that letter by 1
                start+=1
                end+=1
        return False