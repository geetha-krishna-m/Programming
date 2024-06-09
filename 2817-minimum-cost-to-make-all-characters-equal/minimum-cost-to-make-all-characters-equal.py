class Solution:
    def minimumCost(self, s: str) -> int:
        cost,n = 0,len(s)
        for i in range(1,len(s)):
            if(s[i-1] == s[i]):
                continue
            cost += min(i,n-i)
        return cost