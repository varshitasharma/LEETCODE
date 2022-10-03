class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for i in range(1,len(strs)):
            curRes=''
            for j,k in zip(range(len(res)), range(len(strs[i]))):
                if res[j] == strs[i][k] :
                    curRes+=res[j]
                else: break
            res = curRes
                
            
        return res
                    