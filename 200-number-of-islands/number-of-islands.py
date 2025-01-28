class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        # visited = set()
        def checkBoundaries(i,j):
            if(i>=m or j>=n or i<0 or j<0):
                return True
            return False
        def traverseIsland(i,j):
            if(checkBoundaries(i,j) or grid[i][j] == "0"):
                return
            # visited.add((i,j))
            grid[i][j] = "0"
            traverseIsland(i+1,j)
            traverseIsland(i,j+1)
            traverseIsland(i-1,j)
            traverseIsland(i,j-1)
        islandCount = 0
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == "1"):
                    islandCount += 1
                    traverseIsland(i,j)
        return islandCount