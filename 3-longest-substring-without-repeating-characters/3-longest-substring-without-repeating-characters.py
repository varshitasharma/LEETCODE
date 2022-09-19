class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen, start, occur = 0, 0, defaultdict(int)
        for end, ch in enumerate(s):
            if ch in occur.keys() and occur[ch] >= start:
                start = occur[ch]+1
            maxLen = max(maxLen, end-start+1)
            occur[ch] = end
        return maxLen