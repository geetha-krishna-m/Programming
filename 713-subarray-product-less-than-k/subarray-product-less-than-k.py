class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start = 0
        end = 0
        prod = 1
        ans = 0
        while end<len(nums):
            prod *= nums[end]
            end += 1
            while(start<end and prod>=k):
                prod /= nums[start]
                start += 1
            ans += end-start
        return ans

        