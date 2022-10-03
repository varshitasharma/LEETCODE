class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Storing alphabetically smallest and largest strings, then comparing them both to find longest common subsequence
        m, M, i = min(strs), max(strs), 0
        
        #print(m,M)
        for i in range(min(len(m),len(M))):
            if m[i] != M[i]: 
                break
            else:
                i += 1
        return m[:i]