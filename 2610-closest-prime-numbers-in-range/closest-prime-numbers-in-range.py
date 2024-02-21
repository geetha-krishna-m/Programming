class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isprime(num):
            if num == 1:
                return False
            else:
                for i in range(2,int(math.sqrt(num))+1):
                    if(num%i):
                        continue
                    return False
            return True
        res = [-1,-1]
        nexts,maxy = -1,99999999
        while(left<right+1):
            if(left!=2 and left%2==0 or left==1):
                left += 1
                continue
            else:
                if(isprime(left) and nexts!=-1):
                    if((left-nexts)<maxy):
                        res = [nexts,left]
                        maxy = left-nexts
                    nexts = left
                    if(maxy==2):
                        return res
                if(isprime(left) and nexts==-1):
                    nexts = left
                left += 1
        return res
                    

            
            
            
            