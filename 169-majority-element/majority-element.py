class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorityElement = nums[0]
        cnt = 1
        for i in range(1,len(nums)):
            if(nums[i]!=majorityElement):
                cnt -= 1
            else:
                cnt += 1
            if(cnt == 0):
                majorityElement = nums[i]
                cnt = 1
        return majorityElement