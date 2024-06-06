class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if(sum(nums)<target):
            return 0 # array has only positives
        ind,i,ans = 0,0,len(nums)
        k = 0
        for j in range(len(nums)):
            i += nums[j]
            while(i>=target):
                i -= nums[k]
                ans = min(j-k+1,ans)
                k += 1 
        return ans
            

            


        