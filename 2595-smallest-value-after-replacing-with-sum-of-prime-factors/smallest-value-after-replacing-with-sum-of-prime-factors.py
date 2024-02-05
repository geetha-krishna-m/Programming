class Solution:
    def smallestValue(self, n: int) -> int:
        temp = n
        nums = [0]*(n+1)
        for i in range(2, len(nums)):
            if nums[i] == -1:
                continue
            j = i*2
            while j < len(nums):
                nums[j] = -1
                j += i
        primes = []
        for i in range(2, len(nums)):
            if nums[i] == 0:
                primes.append(i)
        slen, cursum = len(primes), 0
        while True:
            i = 0
            temp = n
            key = primes[0]
            cursum = 0
            while n>1 and i<slen:
                while(n%key==0):
                    cursum += key
                    n = n//key
                if n%key != 0:
                    i += 1
                    if i<slen:
                        key = primes[i]
            n = cursum
            if(cursum == temp):
                return cursum
        return cursum
    
    
    