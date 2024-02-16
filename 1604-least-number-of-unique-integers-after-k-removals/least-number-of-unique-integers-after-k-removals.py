class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = collections.Counter(arr)
        x = sorted(d,key = lambda x:d[x])
        x_len =len(x)
        for j,i in enumerate(x):
            if k>=d[i]:
                k = k - d[i]
            else:
                return x_len - (j)
        return 0