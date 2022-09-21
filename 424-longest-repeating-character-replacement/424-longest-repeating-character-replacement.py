class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 0
        maxLen, freq, maxFreq = 0, defaultdict(int), 0
        while(end<len(s)):
            freq[s[end]]+=1
            maxFreq = max(maxFreq, freq[s[end]])# maxFreq may be invalid at some points, but this doesn't matter
                                                # maxFreq will only store the maxFreq reached till now            
            # maintain the substring length and slide the window if the substring is invalid
            if end-start+1 - maxFreq > k:
                freq[s[start]]-=1
                start+=1
            else: maxLen = max(maxLen, end-start+1)
            end+=1
        return maxLen