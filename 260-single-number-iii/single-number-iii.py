class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for i in nums:
            xor ^= i
        a,b = 0,0
        for i in nums:
            if i & (xor&-xor):
                a ^= i
                continue
            b ^= i
        return [a,b]
        