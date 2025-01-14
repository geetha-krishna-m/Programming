class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        s = set()
        n = len(A)
        res = []
        for i in range(n):
            s.add(A[i])
            s.add(B[i])
            res.append(2*(i+1) - len(s))
        return res

        