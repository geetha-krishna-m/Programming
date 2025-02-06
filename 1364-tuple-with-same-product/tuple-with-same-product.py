class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        hashMap = dict()
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                prod = nums[i]*nums[j]
                hashMap[prod] = hashMap.get(prod,0) + 1
        sums = 0
        for i in hashMap:
            sums += 8*((hashMap[i])*(hashMap[i]-1))//2
        return sums