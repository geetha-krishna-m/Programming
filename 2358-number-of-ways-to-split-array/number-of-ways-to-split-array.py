class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0]*n
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] += prefix[i-1]+nums[i]
        cnt = 0
        for i in range(1,n):
            sum_l = prefix[i-1]
            sum_r = prefix[n-1] - prefix[i-1]
            print(sum_l,sum_r)
            if(sum_l>=sum_r):
                cnt += 1
        return cnt
