class Solution:
    def minDeletions(self, s: str) -> int:
        freq = Counter(s)
        count = sorted([val for val in freq.values()], reverse=True)
        delete = 0
        for i in range(1,len(count)):
            while count[i-1] <= count[i] and count[i]: count[i]-=1; delete+=1
        return delete