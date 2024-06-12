class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt_0,cnt_1 = 0,0
        for i in range(len(nums)):
            if(nums[i] == 0):
                cnt_0 += 1
            elif(nums[i] == 1):
                cnt_1 += 1
        for i in range(len(nums)):
            if(cnt_0 >0):
                nums[i] = 0
                cnt_0 -= 1
            elif(cnt_1 > 0):
                nums[i] = 1
                cnt_1 -= 1
            else:
                nums[i] = 2
        return nums
        