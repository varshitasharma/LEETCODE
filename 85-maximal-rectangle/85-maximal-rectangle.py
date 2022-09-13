'''Extension of Largest Rectangle in histogram'''
'''Every row in the matrix is viewed as the ground with some buildings on it. The building height is the count of consecutive 1s from that row to above rows. The rest is then the same as this solution for largest rectangle in histogram'''

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        '''
        **For example 1 in que: it'll look like this after updating heights of building at each row**
        Each row has heights of bars of histogram on that level of the row.
        [1, 0, 1, 0, 0]
        [2, 0, 2, 1, 1]
        [3, 1, 3, 2, 2]
        [4, 0, 0, 3, 0]  # Height of building at i=0, j= 0 is 4

        '''
        
        '''This block updates the matrix. Each cell of every row stores height of the building(consecutive 1's from that cell to above cells).'''
        
        for i in range( rows):
            for j in range(cols):
                matrix[i][j] = int(matrix[i][j])
                if i>0 and matrix[i][j] ==1 and matrix[i-1][j]!= 0:
                    matrix[i][j] =  1 +  matrix[i-1][j] 
            print(matrix[i])
              
        '''Here we perform the same operation as for Largest area of histogram, for every row, considering each row as array of heights of the histogram at that row level'''
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
