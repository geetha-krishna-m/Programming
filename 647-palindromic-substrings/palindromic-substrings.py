class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        for i in range(n):
            for j in range(i,n):
                k = s[i:j+1]
                if(k == k[::-1]):
                    cnt += 1
        return cnt
        