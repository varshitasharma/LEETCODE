class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        for i in range( rows):
            for j in range(cols):
                matrix[i][j] = int(matrix[i][j])
                if i>0 and matrix[i][j] ==1 and matrix[i-1][j]!= 0:
                    matrix[i][j] =  1 +  matrix[i-1][j] 
              
        # print(matrix)
        maxArea = 0
        for row in matrix:
            row.append(0)
            stack = [-1]
            i = 0
            for i, height in enumerate(row):
                while(height<row[stack[-1]]):
                    h = row[stack.pop()]
                    width = i - 1 - stack[-1]
                    maxArea = max(maxArea, h*width)
                stack.append(i)
                
        return maxArea
#         for i in range(rows):
#             for j in range(cols):
#                 stack=[-1]
                
#                 while
                
                
#         stack = []
        return