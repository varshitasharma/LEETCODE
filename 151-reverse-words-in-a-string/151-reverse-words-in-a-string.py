class Solution:
    def reverseWords(self, s: str) -> str:
        reverseS = s.split()
        return ' '.join(list(reverseS[::-1]))
        