from collections import defaultdict 
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = dict()
        for i in s:
            d[i] = d.get(i,0) + 1
        cnt,flag = 0,1
        for i in d:
            cnt += ((d[i]//2) * 2)
            if d[i]%2 == 1 and flag:
                cnt += 1
                flag = 0
        return cnt
            
        