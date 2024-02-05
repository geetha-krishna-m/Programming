class Solution:
    def distinctIntegers(self, n: int) -> int:
        res={n}
        for i in range(n,1,-1):
            for j in range(2,i):
                if i%j == 1:
                    res.add(j)
        return len(res)
        