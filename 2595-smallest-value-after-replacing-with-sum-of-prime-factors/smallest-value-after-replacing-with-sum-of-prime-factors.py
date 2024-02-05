class Solution:
    def smallestValue(self, n: int) -> int:
        while True:
            temp = n
            cursum = 0
            while n>1:
                while(n%2==0):
                    cursum += 2
                    n = n//2
                for i in range(3,n+1,2):
                    while(n%i == 0):
                        cursum += i
                        n = n//i
            n = cursum
            if(cursum == temp):
                return cursum
        return cursum
    
    
    