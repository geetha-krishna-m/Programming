class Solution:
    def minimumCost(self, s: str) -> int:
        cost,n = 0,len(s)
        for i in range(len(s)-1):
            if(s[i] == s[i+1]):
                continue
            cost += min(i+1,n-i-1)
        return cost