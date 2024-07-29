class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if(len(nums)<=4):
            return 0
        nums.sort()
        one = nums[-4] - nums[0]  # fourth largest - minimum (3 largest changed to minimum)
        two = nums[-3] - nums[1]
        three = nums[-2] - nums[2]
        four = nums[-1] - nums[3]
        return min(min(one,two),min(three,four))