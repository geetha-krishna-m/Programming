class Solution:
    def isValidSudoku(self, grid: List[List[str]]) -> bool:
        n = len(grid)
        ans = True
        def squares(r_i,r_j,c_i,c_j):
            vis = set()
            print(r_i,r_j,c_i,c_j)
            for i in range(r_i,r_j):
                for j in range(c_i,c_j):
                    if(grid[i][j]!="."):
                        if(grid[i][j] in vis):
                            return False
                        vis.add(grid[i][j])
            return True
        for i in range(0,n,3):
            for j in range(0,n,3):
                ans = ans and squares(i,i+3,j,j+3)
                if(not ans):
                    return False
        # column traverse
        for i in range(n):
            vis = set()
            for l in range(n):
                if(grid[i][l]!="."):
                    if(grid[i][l] in vis):
                        print(grid[i][l],vis)
                        return False
                    vis.add(grid[i][l])
        # row traverse
        for i in range(n):
            vis = set()
            for l in range(n):
                if(grid[l][i]!="."):
                    if(grid[l][i] in vis):
                        print(grid[i][l],vis)
                        return False
                    vis.add(grid[l][i])
        return True