class Solution:
    def check(self,nums,k):
        s = 0
        ans = 0
        j = 0
        for i in range(len(nums)):
            s += (nums[i]%2)
            while(s>k):
                s -= (nums[j]%2)
                j += 1
            ans += (i-j+1)
        return ans
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.check(nums,k) - self.check(nums,k-1)
        