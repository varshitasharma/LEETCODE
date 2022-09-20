class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lenS, lenT = len(s), len(t)
        if lenS<lenT: return ''
        freqT, start, minLen, ans = Counter(t), 0, 100001, ''
        count = len(freqT)
        # print(freqT)
        for end, ch in enumerate(s):
            if ch in freqT.keys():
                freqT[ch]-=1
                if freqT[ch] == 0: count-=1
                if count == 0:
                    i = start
                    while( count == 0):
                        if s[i] in freqT.keys():
                            freqT[s[i]]+=1
                            if freqT[s[i]] == 1:
                                if minLen > end-i+1:
                                    ans = s[i:end+1]
                                    minLen = end-i+1
                                start = i+1
                                count += 1
                        i+=1
        return ans
                
                        