class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if(len(nums)<=4):
            return 0
        w,x,y,z,a,b,c,d = -999999,-999999,-999999,-999999,999999,999999,999999,999999
        for i in range(len(nums)):
            if w<nums[i]:
                z,y,x,w = y,x,w,nums[i]
            elif x<nums[i]:
                z,y,x = y,x,nums[i]
            elif y<nums[i]:
                z,y = y,nums[i]
            elif z<nums[i]:
                z = nums[i]
            
            if(a>nums[i]):
                d,c,b,a = c,b,a,nums[i]
            elif(b>nums[i]):
                d,c,b = c,b,nums[i]
            elif(c>nums[i]):
                d,c = c,nums[i]
            elif(d>nums[i]):
                d = nums[i]
        return min(w-d,x-c,y-b,z-a)