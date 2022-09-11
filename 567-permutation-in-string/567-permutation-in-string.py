class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        letter_count, letter_count_s1, start, end, len_s1 = collections.Counter(s1), collections.Counter(s1), 0, 0, len(s1)
        count = len(letter_count_s1)  # count Stores number of distinct letters of s1 available to use in current window
        # letter_count_s1 contains count of all characters in s1
        while(end<len(s2)):
            if letter_count_s1[s2[end]] > 0: # if current character is present is s1
                letter_count[s2[end]]-=1   # decrement count of that character for current window
                if letter_count[s2[end]] == 0:  # if count of that character for current window becomes zero -> #occurrences of that                                                            letter in current window is same as that in string s1, so decrement available letters count by 1
                    count-=1
            if end-start+1 < len_s1:
                end+=1
            elif end-start+1 == len_s1:
                if count == 0: return True   #  #if letters availabe become zero in current window -> #occurrences of all                                                            letters in current window is same as that in string s1, so return True
                if letter_count_s1[s2[start]] > 0:  #  #before moving the window check if the start index(which will be out of window as window moves) contributes to letter count. 
                    letter_count[s2[start]]+=1  #If yes then increase the letter count of that letter by 1 so that it can be used again
                    if letter_count[s2[start]] == 1: #If it is 1, means it was zero before, i.e. letter was unavailabe but now it is available so incerement available count by 1
                        count+=1 
                start+=1
                end+=1
        return False
        
        
        
        
        # letter_count, letter_count_s1, start, end, len_s1 = collections.Counter(''), collections.Counter(s1), 0, 0, len(s1)
        # # letter_count_s1 contains count of all characters in s1
        # while(end<len(s2)):
        #     if letter_count_s1[s2[end]] > 0: # if current character is present is s1
        #         letter_count[s2[end]]+=1   # Increment count of that character for current window
        #     if end-start+1 < len_s1:
        #         end+=1
        #     elif end-start+1 == len_s1:
        #         if letter_count == letter_count_s1: return True   #  #if Counter of the actual matches with Counter of substring in current window -> the current substring is a permutation of s1
        #         if letter_count_s1[s2[start]] > 0: letter_count[s2[start]]-=1  #  #before moving the window check if the start index(which will be out of window as window moves) contributes to letter count. If yes then decrease the letter count of that letter by 1
        #         start+=1
        #         end+=1
        # return False