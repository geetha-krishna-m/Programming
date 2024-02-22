class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        res = [0 for i in range(n)]
        for i in trust:
            res[i[1]-1] += 1
            res[i[0]-1] -= 1
        for i in range(n):
            if(res[i]==(n-1)):
                return i+1
        return -1
