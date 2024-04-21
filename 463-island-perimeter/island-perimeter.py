class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        sums = 4*row*col
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    cnt += 1
                    continue
                if i-1>-1:
                    if(grid[i][j]==1 and grid[i-1][j] == 1):
                        sums -= 1
                if i+1 < row:
                    if(grid[i][j]==1 and grid[i+1][j] == 1):
                        sums -= 1
                if j-1>-1:
                    if(grid[i][j]==1  and grid[i][j-1] == 1):
                        sums -= 1
                if j+1<col:
                    if(grid[i][j]==1  and grid[i][j+1] == 1):
                        sums -= 1
        return sums - cnt*4
                

                    
        