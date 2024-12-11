class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        def binary_right(nums,val):
            left,right = 0, n
            while(left<right):
                mid = left + (right-left)//2
                if(nums[mid]<=val):
                    left = mid + 1
                else:
                    right = mid
            return left
        for i in range(n):
            ind = binary_right(nums,nums[i]+2*k)
            ans = max(ans,ind-i)
        return ans