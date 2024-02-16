class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = collections.Counter(arr)
        x = sorted(d,key = lambda x:d[x])
        for i in x:
            if k>=d[i]:
                k = k - d[i]
                if k>=0:
                    del d[i] 
            if k<=0:
                break       
        return len(d)