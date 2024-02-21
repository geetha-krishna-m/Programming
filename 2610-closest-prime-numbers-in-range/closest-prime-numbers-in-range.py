class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isprime(num):
            if(num==1):
                return False
            for i in range(2,int(math.sqrt(num))+1):
                if(num%i):
                    continue
                return False
            return True
        res = [-1,-1]
        nexts,maxy = -1,99999999
        if((left!=2 and left%2==0)):
            left += 1
        if(left<2 and right>2):
            return [2,3]
        while(left<right+1):
            if(isprime(left) and nexts!=-1):
                if((left-nexts)<maxy):
                    res = [nexts,left]
                    maxy = left-nexts
                    if(maxy==2):
                        return res
                nexts = left
            if(isprime(left) and nexts==-1):
                nexts = left
            if(left<3):
                left += 1
                continue
            left += 2
        return res
                    

            
            
            
            