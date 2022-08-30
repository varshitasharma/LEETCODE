class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = collections.Counter(magazine)
        for ch in ransomNote:
            if d[ch] == 0:
                return False
            d[ch]-=1
        return True