from collections import defaultdict
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = defaultdict(int)
        for i in arr:
            d[i%k] += 1
        l,r = 1,k-1
        while(l<r):
            if(d[l]!=d[r]):
                return False
            l += 1
            r -= 1
        if(l==r):
            if(d[l]%2!=0):
                return False
        return True

