class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = collections.Counter(magazine)
        for ch in ransomNote:
            if ch not in d or d[ch] == 0:
                return False
            d[ch]-=1
        return True