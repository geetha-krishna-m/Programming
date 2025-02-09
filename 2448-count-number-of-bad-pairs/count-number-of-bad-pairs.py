class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        hash_map = dict()
        possible_values = ((n)*(n-1))//2
        for i in range(n):
            diff = i-nums[i]
            hash_map[diff] = hash_map.get(diff,0) + 1
        for i in hash_map:
            x = hash_map[i]
            possible_values -= (x*(x-1))//2
        return possible_values