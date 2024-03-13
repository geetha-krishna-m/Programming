class Solution:
    def pivotInteger(self, n: int) -> int:
        prefixSum = []
        sums = 0
        for i in range(n,0,-1):
            sums += i
            prefixSum.append(sums)
        sums = 0
        for i in range(1,n+1):
            sums += i
            if(sums == prefixSum[n-i]):
                return i
        return -1    