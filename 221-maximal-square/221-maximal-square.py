class Solution:
    '''https://leetcode.com/problems/maximal-square/discuss/600149/Python-Thinking-Process-Diagrams-DP-Approach'''
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols, maxSide = len(matrix), len(matrix[0]), 0
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = int(matrix[i][j])
                if i>0 and j>0:
                    if matrix[i][j]: matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1]) +1
                maxSide = max(maxSide, matrix[i][j])
        print(matrix)
        return maxSide**2