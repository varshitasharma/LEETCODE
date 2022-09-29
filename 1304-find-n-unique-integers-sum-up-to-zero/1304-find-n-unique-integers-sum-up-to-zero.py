class Solution:
    def sumZero(self, n: int) -> List[int]:
        output=[]
        for i in range(1,n):
            output.append(i)
        output.append(-(n*(n-1))//2)
        return output