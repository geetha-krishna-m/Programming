class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        mid = len(nums)//2
        if(nums[mid] == k):
            return 0
        elif(nums[mid]<k):
            cost = 0
            while(mid<len(nums) and nums[mid]<k):
                cost += abs(nums[mid]-k)
                mid += 1
        else:
            cost = 0
            while(mid>-1 and nums[mid]>k):
                cost += abs(nums[mid]-k)
                mid -= 1
        return cost
            
        