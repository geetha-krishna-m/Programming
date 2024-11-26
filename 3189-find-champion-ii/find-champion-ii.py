class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        dict()
        m = len(edges)
        d = set()
        for i in range(m):
            x,y = edges[i][0],edges[i][1]
            d.add(y)
        if(len(d) != n-1):
            return -1
        else:
            for i in range(n):
                if i not in d:
                    return i
            return -1
        