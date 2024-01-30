class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j,n= 0,len(t)
        for i in s:
            if j<n and t[j] == i:
                j += 1
        return n - j
                
        