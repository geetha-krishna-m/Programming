class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalTriangle = []
        for i in range(1,numRows+1):
            intermediateRow = [0 for _ in range(i)]
            for j in range(i):
                if(j==0 or j==i-1):
                    intermediateRow[j] = 1
                else:
                    intermediateRow[j] = pascalTriangle[i-2][j-1] + pascalTriangle[i-2][j]
            pascalTriangle.append(intermediateRow)
            print(pascalTriangle)
        return pascalTriangle
