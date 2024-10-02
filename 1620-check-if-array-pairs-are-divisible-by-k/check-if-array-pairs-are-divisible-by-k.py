from collections import defaultdict
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = defaultdict(list)
        for i in arr:
            d[i%k].append(i)
        l,r = 1,k-1
        while(l<r):
            if(len(d[l])!=len(d[r])):
                return False
            l += 1
            r -= 1
        if(l==r):
            if(len(d[l])%2!=0):
                return False
        return True

