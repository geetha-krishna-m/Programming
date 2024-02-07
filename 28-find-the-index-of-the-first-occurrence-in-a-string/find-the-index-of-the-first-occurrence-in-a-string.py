class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        i,j = 0,0
        if(n>=h and haystack!=needle):
            return -1 
        while i<h:
            if(haystack[i]==needle[j]):
                j += 1
            else:
                i = i - j
                j = 0
            if(j == n):
                return i-n+1
            i += 1
        return -1