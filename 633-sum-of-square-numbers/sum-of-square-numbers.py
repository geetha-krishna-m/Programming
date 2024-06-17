class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a,b=0,int(c**0.5)+1
        while(a<=b):
            check = a**2+b**2
            if(check>c):
                b = b - 1
            elif(check<c):
                a = a + 1
            else:
                return True
        return False