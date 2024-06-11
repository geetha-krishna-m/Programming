from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = Counter(arr1)
        res = []
        for i in arr2:
            while(d[i]!=0):
                res.append(i)
                d[i] -= 1
        for i in sorted(d):
            while(d[i] != 0):
                res.append(i)
                d[i] -= 1
        return res      