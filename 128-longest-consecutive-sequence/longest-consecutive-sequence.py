class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        longest = 0
        for i in uniqueNums:
            if i+1 not in uniqueNums:
                x = i
                cnt = 1
                while x-1 in uniqueNums:
                    cnt += 1
                    x -= 1
                longest = max(longest,cnt)
        return longest
