class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = collections.Counter(arr)
        x = sorted(d,key = lambda x:d[x])
        cnt = 0
        for i in x:
            if k>=d[i]:
                k = k - d[i]
                cnt += 1
            if k<=0:
                break     
        return len(d) - cnt