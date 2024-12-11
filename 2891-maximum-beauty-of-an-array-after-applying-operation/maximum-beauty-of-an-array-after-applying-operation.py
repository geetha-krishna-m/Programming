class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        maxy = max(nums) + 2*k
        ans = 1
        prefix = [0]*(maxy+2)
        for i in range(n):
            prefix[max(nums[i]-k,0)] += 1
            prefix[min(nums[i]+k,maxy)+1] -= 1
        for i in range(1,maxy+2):
            prefix[i] += prefix[i-1] 
            ans = max(ans,prefix[i])
        return ans