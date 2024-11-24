class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if(n<=0):
            return False
        def recurse(n):
            if(n==1):
                return True
            return (not(n%3)) and recurse(n/3)
        return recurse(n)