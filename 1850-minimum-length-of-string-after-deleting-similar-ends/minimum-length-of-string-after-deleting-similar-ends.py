class Solution:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s) - 1
        while(i<j):
            k ,d = s[i],s[j]
            temp = i
            jtemp = j
            while( temp<len(s)-1 and s[temp]==s[temp+1]):
                temp = temp + 1
                k = s[temp]
            while(jtemp>0 and s[jtemp] == s[jtemp-1] and (j-1)!=(i+1)):
                jtemp = jtemp - 1
                d = s[j]
            if(k != d):
                return j - i + 1
            i = temp + 1
            j = jtemp - 1
        if(j-i>=0):
            return j-i+1
        return 0

        