class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        left , right = 0, len(matrix[0])-1
        top, bottom= 0, len(matrix)-1
        while(0<=top<=bottom and 0<=left<=right):
            # print('top')
            for j in range(left, right+1):
                output.append(matrix[top][j])
            for i in range(top+1,bottom+1):
                output.append(matrix[i][right])
            if bottom != top:
                for j in range(right-1, left-1, -1 ):
                    output.append(matrix[bottom][j])
            if left != right:
                for i in range(bottom-1, top, -1):
                    output.append(matrix[i][left])
            top+=1
            bottom-=1
            left+=1
            right-=1
            # print(output)
        return output