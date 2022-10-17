class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def calcArea(i, j):
            if not (-1<i<rows) or not(-1<j<cols) or grid[i][j] == 0: return 0
            grid[i][j] = 0
            return 1 + calcArea(i, j-1) + calcArea(i-1,j) + calcArea(i, j+1) + calcArea(i+1,j)
            
        maxArea, rows, cols = 0, len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]: maxArea = max(maxArea, calcArea(i,j))    
        return maxArea
        