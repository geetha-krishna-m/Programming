class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict()
        n = len(s)
        for i in s:
            d[i] = d.get(i,0) + 1
        for j,i in enumerate(s):
            if d[i] == 1:
                return j
        return -1
        