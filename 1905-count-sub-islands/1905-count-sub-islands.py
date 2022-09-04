class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row, col = len(grid1), len(grid1[0])
        check = [[0 for _ in range(col)] for _ in range(row)]
        count = 0
        
        def check_island(index1, index2):
            if index1<0 or index1>=row or index2<0 or index2>=col  or check[index1][index2]  or grid2[index1][index2] == 0 :
                return True
            check[index1][index2] = 1
            

            
            # return check_island(index1-1, index2) and check_island(index1, index2-1) and check_island(index1, index2+1) and check_island(index1+1, index2)
            up = check_island(index1-1, index2)
            left = check_island(index1, index2-1)        
            right = check_island(index1, index2+1)
            down = check_island(index1+1, index2)
            # print(index1, index2, up,left,right,down)
            if grid1[index1][index2]==0: 
                return False
            return up and left and right and down
        # print(row, col)
        for i in range(row):
            for j in range(col):
                # print(i,j)
                if grid2[i][j] == 1 and grid1[i][j] == 1 and not check[i][j]:
                    # print(i,j)
                    if check_island(i,j): count+=1
        return count
                
                