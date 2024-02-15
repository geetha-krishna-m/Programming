class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # nums.sort()
        # n = len(nums)
        # sums = sum(nums)
        # for i in range(n-1,-1,-1):
        #     if(nums[i]<sums-nums[i]):
        #         return sums
        #     sums = sums-nums[i]
        # return -1
        sums = sum(nums)
        n = len(nums)
        while True:
            if not nums:
                return -1
            x = max(nums)
            if(sums-x<=x):
                nums = [i for i in nums if i!=x]
                sums = sums - x*(n-len(nums))
                n = len(nums)
            else:
                return sums
        return -1
                
            

            