class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        sums = sum(nums)
        for i in range(n-1,-1,-1):
            if(nums[i]<sums-nums[i]):
                return sums
            sums = sums-nums[i]
        return -1