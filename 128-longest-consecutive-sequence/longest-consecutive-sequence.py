class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in nums:
                nextNum = num + 1
                while nextNum in nums:
                    nextNum += 1
                res = max(res, nextNum - num)
        return res