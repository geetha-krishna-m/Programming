class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        longest = 0
        for i in uniqueNums:
            if i+1 not in uniqueNums:
                x = i
                while x-1 in uniqueNums:
                    x -= 1
                longest = max(longest,i-x+1)
        return longest
