class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalTriangle = []
        for i in range(numRows):
            intermediateRow = [0 for _ in range(i+1)]
            for j in range(i+1):
                if(j==0 or j==i):
                    intermediateRow[j] = 1
                else:
                    intermediateRow[j] = pascalTriangle[i-1][j-1] + pascalTriangle[i-1][j]
            pascalTriangle.append(intermediateRow)
        return pascalTriangle
