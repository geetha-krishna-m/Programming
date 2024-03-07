class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d=dict()
        g=set()
        for i in range(len(s)):
            if(s[i] in d):
                if(d[s[i]] != t[i]):
                    return False
            elif(t[i] in g):
                return False
            else:
                d[s[i]] = t[i]
                g.add(t[i])
        return True
        