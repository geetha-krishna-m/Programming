class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = collections.Counter(arr)
        x = sorted(d,key = lambda x:d[x])
        for i in x:
            while k!=0 and d[i]!=0:
                d[i] -= 1
                k -= 1
            if k==0:
                break    
        return sum(1 for i in d.values() if i!=0)