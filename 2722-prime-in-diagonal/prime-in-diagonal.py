class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def prime(num):
            if(num==1):
                return False
            for i in range(2,int(num**0.5)+1):
                if num%i==0:
                    return False
            return True
        maxy = 0
        for i in range(len(nums)):
            if(prime(nums[i][i])):
                maxy = max(maxy,nums[i][i])
            if(prime(nums[i][len(nums)-i-1])):
                maxy = max(maxy,nums[i][len(nums)-i-1])
        return maxy
        