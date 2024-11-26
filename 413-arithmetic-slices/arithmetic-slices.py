class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if(n<3):
            return 0
        res,i = 0,0
        while(i<n-2):
            j = i + 2
            while(j<n):
                if(nums[j-1] - nums[j-2] == nums[j] - nums[j-1]):
                    j = j + 1
                else:
                    break
            diff = j - i
            print(i,j,diff)
            if(diff>=3):
                res += (diff*(diff+1))//2 + 1 - (2*diff)
            i = j-1
        return res
                
        