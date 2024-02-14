class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num = [0 for i in range(n)]
        j = 0
        for i in range(n):
            if(nums[i]>0):
                num[j] = nums[i]
                j += 2
        j = 1
        for i in range(n):
            if(nums[i]<0):
                num[j] = nums[i]
                j += 2
        return num

            
                