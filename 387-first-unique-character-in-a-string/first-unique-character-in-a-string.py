class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict()
        v = set()
        n = len(s)
        for i in range(n):
            if s[i] not in d:
                d[s[i]] = i
            else:
                if d[s[i]] not in v:
                    v.add(d[s[i]])
                v.add(i)
        for i in range(n):
            if i not in v:
                return i
        return -1
                
                