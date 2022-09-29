class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev,minTime = 0,0
        for i in range(1,len(colors)):
            if colors[i] == colors[prev]: 
                if neededTime[prev] <= neededTime[i]: 
                    minTime+=neededTime[prev]
                    prev = i
                else:
                    minTime+=neededTime[i]
            else: prev = i
        return minTime
                    