class Solution:
    def minimumLength(self, s: str) -> int:
        c = [0]*26
        n,cnt = len(s),0
        for i in range(n):
            c[ord(s[i])-97] += 1
        for i in range(26):
            if(c[i] and c[i]%2):
                cnt += (c[i]-1)
            if(c[i] and not c[i]%2):
                cnt += (c[i]-2)
        return n-cnt

        