class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for i in nums:
            xor ^= i
        a,b = 0,0
        """(xor & -xor) gives you the right most set bit in the result and we can use this to divide the two unique numbers in the nums as their result of xor will never be 0 as they are different and there must be atleast one set bit between them -- super idea"""
        for i in nums:
            if i & (xor&-xor): 
                a ^= i
                continue
            b ^= i
        return [a,b]
        