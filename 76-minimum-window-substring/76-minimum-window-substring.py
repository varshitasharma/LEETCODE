class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lenS, lenT = len(s), len(t)
        if lenS<lenT: return ''
        freqT, start, minLen, ans = Counter(t), 0, 100001, ''
        count = len(freqT)
        '''Iterate the string and whenever you find a char that's present in 't', decrement it's count in freqT. count var will have count of total distinct characters. As count becomes 0, you'll find an answer, then iterate the answer string from left and decrease the size by removing extra characters that aren't present in 't' until you see one char that's present in t  '''
        for end, ch in enumerate(s):
            if ch in freqT.keys():
                freqT[ch]-=1      # keeps reducing count of char as you see it. It can become negative also. 
                                # As it becomes -ve, it signifies extra chars that we find of that letter, which we can remove while calculating ans
                if freqT[ch] == 0: count-=1  # as freq of a char becomes 0 then we decrement the count of characters to find by 1
                if count == 0: # candidate answer found
                    i = start           # now iterating from start to find the first occurrence of any letter from 't', 
                    while( count == 0):   #so that we get smallest possible substring from current window, by removing extra letters before that index
                        if s[i] in freqT.keys():   # if current char is present in 't'
                            freqT[s[i]]+=1    # increment count 
                            if freqT[s[i]] == 1: # As count becomes 1 from 0, => This char has to be first index in our window 
                                                 # & we need all letters from this index till end in our ans
                                                # and we can remove all letters before this to reduce substring size
                                if minLen > end-i+1:  # now calculate length from i  till end
                                    ans = s[i:end+1]  
                                    minLen = end-i+1
                                start = i+1    # Also update next starting point to, char next to first letter in current window
                                count += 1
                        i+=1
        return ans
                
                        