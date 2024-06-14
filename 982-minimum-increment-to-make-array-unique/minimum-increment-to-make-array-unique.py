class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        for i in range(len(nums)-1):
            if(nums[i+1]-nums[i]<=0):
                diff = nums[i+1]
                nums[i+1] = nums[i] + 1
                cnt += nums[i+1] - diff
        return cnt 


        