class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProd = []
        suffixProd = []
        res = [0 for i in range(len(nums))]
        pprod , sprod = 1,1
        for i in range(len(nums)):
            pprod *= nums[i]
            sprod *= nums[len(nums)-i-1]
            prefixProd.append(pprod)
            suffixProd.append(sprod)
        suffixProd = suffixProd[::-1]
        res[0] , res[len(nums)-1] = suffixProd[1] , prefixProd[len(nums)-2]  
        for i in range(1,len(nums)-1):
            res[i] = (prefixProd[i-1]*suffixProd[i+1])
        return res
