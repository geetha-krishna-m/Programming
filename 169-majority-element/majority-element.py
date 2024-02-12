class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = nums[0]
        n = len(nums)
        for i in range(n):
            if nums[i] == candidate or count == 0:
                if(count == 0):
                    candidate = nums[i]
                count += 1
            else:
                count -= 1
        return candidate