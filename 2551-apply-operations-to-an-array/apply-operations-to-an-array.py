class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums) # this is the length of the array
        j = 0 # used to swap
        for i in range(n-1):
            if(nums[i] == nums[i+1]):
                nums[i] *= 2
                nums[i+1] = 0
        for i in range(n):
            if(nums[i]!=0):
                nums[i],nums[j] = nums[j],nums[i]
                j = j + 1
        return nums