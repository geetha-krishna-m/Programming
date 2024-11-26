class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if(n<3):
            return 0
        res,r = 0,1
        start = 0
        diff = nums[1] - nums[0]
        while(r<n):
            if(nums[r]-nums[r-1] == diff):
                r += 1
            else:
                if(r-start>=3):
                    res += ((r-start)*(r-start+1))//2 - (2*(r-start)) + 1
                start = r-1
                diff = nums[r] - nums[r-1]
        if(r-start>=3):
            res += ((r-start)*(r-start+1))//2 - (2*(r-start)) + 1
        return res
                
                
        