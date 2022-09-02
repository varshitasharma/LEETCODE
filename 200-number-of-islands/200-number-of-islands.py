class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col, count = len(grid), len(grid[0]), 0
        check = [[0 for _ in range(col) ] for _ in range(row)]
        def dfs(i,j):
            if i<0 or i>row-1 or j<0 or j>col-1 or check[i][j] or grid[i][j] == '0':
                return
            check[i][j] = 1
            dfs(i, j+1)
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i, j-1)
            
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and not check[i][j] :
                    dfs(i, j)
                    count += 1
        return count
        