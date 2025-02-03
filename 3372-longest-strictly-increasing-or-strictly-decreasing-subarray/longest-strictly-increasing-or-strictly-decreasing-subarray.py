class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxy,count_i,count_d = 0,0,0
        for i in range(n-1):
            if(nums[i]<nums[i+1]):
                count_d = 0
                count_i += 1
            if(nums[i]>nums[i+1]):
                count_i = 0
                count_d += 1
            if(nums[i]==nums[i+1]):
                count_i,count_d = 0,0
            maxy = max(count_i,count_d,maxy)
        return maxy+1


        