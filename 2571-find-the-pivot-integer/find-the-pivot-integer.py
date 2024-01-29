class Solution:
    def pivotInteger(self, n: int) -> int:
        sums = (n*(n+1))//2
        cumi = 0
        for i in range(1,n+1):
            cumi += i
            if(cumi == sums-cumi+i):
                return i
        return -1
            
        