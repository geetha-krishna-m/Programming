class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        res,cnt = [],1
        d = dict()
        for val in sorted(arr):
            if(val not in d):
                d[val] = cnt
                cnt = cnt + 1
        for i in range(len(arr)):
            res.append(d[arr[i]])
        return res
        