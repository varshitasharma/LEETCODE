class Solution:
#     Flood fill or graph expansion
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def paint(grid,i,j):
            if not 0<=i<len(grid) or not 0<=j<len(grid[0]):
                return 
            if grid[i][j]==1:
                grid[i][j] = 2
                paint(grid,i-1,j)
                paint(grid,i+1,j)
                paint(grid,i,j-1)
                paint(grid,i,j+1)
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    paint(grid,i,j)
                    break 
            else:
                continue 
            break 
        
        # print(grid)
        def expand(grid,i,j,n):
            # print(i,j)
            if not 0<=i<len(grid) or not 0<=j<len(grid[0]):
                return   
            if grid[i][j]==0:
                grid[i][j] = n+1
            return grid[i][j]==1
        
        n = 2
        while True:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    # print('in',i,j,n)
                    if grid[i][j]==n and (expand(grid,i-1,j,n) or expand(grid,i+1,j,n) or expand(grid,i,j+1,n) or\
                                          expand(grid,i,j-1,n)):
                        return n-2
                    # print(grid)
            n += 1
#         def check_island(i,j):
#             # print(i,j)
#             if i<0 or j<0 or i>=row or j>= col or grid[i][j] == 0 or check[i][j]:
#                 return
            
#             check[i][j] = 1
# #             left, top, right, down
#             check_island(i,j-1)
#             check_island(i-1,j)
#             check_island(i,j+1)
#             check_island(i+1,j)
            
#         def flip_count(i,j):
#             if i<0 or j<0 or i>= row or j>=col or (grid[i][j] == 1 and check[i][j]==1) :
#                 return 101
#             # if grid[i][j] == 1 and not check[i][j]:
#             #     # print('1 found')
#             #     return 0
            
#             left, top,right, down = 101,101,101,101
#             if j>0:
#                 if grid[i][j-1] == 0:
#             # if j>0:
#                     # print('l',i,j)
#                     grid[i][j-1] = -1
#                     left = 1 + flip_count(i,j-1)
#                     grid[i][j-1] = 0
#                 elif grid[i][j-1] == 1 and not check[i][j-1]:
#                     # print('1 found')
#                     return 0
#             if i>0 :
#                 if grid[i-1][j] == 0:
#             # if i>0:
#                     grid[i-1][j] = -1
#                     top = 1 + flip_count(i-1,j)
#                     grid[i-1][j] = 0
#                 elif grid[i-1][j] == 1 and not check[i-1][j]:
#                     # print('1 found')
#                     return 0
                
#             if j<col-1:
#                 if grid[i][j+1] == 0:
#             # # if j<col-1:
#                     grid[i][j+1] = -1
#                     # print('r',i,j)
#                     right = 1+flip_count(i,j+1)
#                     grid[i][j+1] =0
#                 elif grid[i][j+1] == 1 and not check[i][j+1]:
#                     # print('1 found')
#                     return 0
#             if i<row-1:
#                 if grid[i+1][j] == 0:
#             # if i<row-1:
#                     grid[i+1][j] = -1
#                     # print('d',i,j)
#                     down = 1+flip_count(i+1,j)
#                     grid[i+1][j] = 0
#                 elif grid[i+1][j] == 1 and not check[i+1][j]:
#                     # print('1 found')
#                     return 0
#             return min(down,min(right,min(left,top)))
        
#         row, col = len(grid), len(grid[0])
#         check = [[0 for _ in range(col)] for _ in range(row)]
#         min_flips = 101
#         flag =0 
        
#         for i in range(row):
#             for j in range(col):
#                 if grid[i][j] == 1:
#                     check_island(i,j)
#                     first_point = (i,j)
#                     flag = 1
#                     break
#             if flag : break
                
#         # print(check)
#         for i in range(first_point[0],row):
#             for j in range(first_point[1],col):
#                 if check[i][j] == 1:
#                     check[i][j] = 2
#                     # print(i,j)
#                     cur = flip_count(i,j)
#                     # print(cur)
#                     check[i][j] = 1
#                     min_flips = min(min_flips, cur)
#         return min_flips