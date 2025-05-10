class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j = 0,1
        n = len(nums)
        while(j < n):
            if(nums[i]!=0):
                i = i + 1
            else:
                if(nums[j]!=0):
                    nums[i],nums[j] = nums[j],nums[i]
                    i = i + 1
            j = j + 1
        return nums
