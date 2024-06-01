class Solution:
    def scoreOfString(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)-1):
            cnt += abs(ord(s[i]) - ord(s[i+1]))
        return cnt
        