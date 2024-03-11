class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = ""
        d = dict()
        for i in s:
            d[i] = d.get(i,0) + 1
        for i in order:
            if i in d:
                res += i*d[i]
                d[i] = 0
        for i in d:
            if d[i]:
                res += d[i]*i
        return res
        