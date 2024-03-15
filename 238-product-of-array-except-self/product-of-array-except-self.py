class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0 for i in range(len(nums))]
        pprod , sprod = 1,1
        for i in range(len(nums)):
            pprod *= nums[i]
            res[i] = pprod
        for i in range(len(nums)-1):
            res[len(nums)-i-1] = sprod*res[len(nums)-i-2]
            sprod *= nums[len(nums)-i-1]
        res[0] = sprod
        return res