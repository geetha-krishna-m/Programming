class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i,j,n = 0,0,len(s)
        while(i<n and j<len(t)):
            if(s[i]==t[j]):
                j += 1
            i += 1
        x = len(t)-j
        return x
        